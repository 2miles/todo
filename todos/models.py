import datetime
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    # one user can have many todos
    # if a user gets deleted their todos get deleted too
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        str = self.title
        if len(str) > 30:
            str = str[:27] + "..."
        return str

    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})

    def clean(self):
        if self.start_date is None:
            self.start_date = timezone.now()

        self.title = self.title.capitalize()
        self.description = self.description.capitalize()

        if self.finish_date and self.completed is False:
            raise ValidationError(
                {"completed": "Task must be completed if finish time is chosen."}
            )

        if self.finish_date:
            if self.finish_date <= self.start_date:
                raise ValidationError(
                    {"finish_date": "Start time must be before finish time."}
                )
            if self.finish_date > timezone.now():
                raise ValidationError(
                    {"finish_date": "Finish time cannot be in the future."}
                )
        super(Todo, self).clean()
