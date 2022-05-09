from django.conf import settings
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
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
        pass
        # return reverse("todo_detail", kwargs={"pk": self.pk})
