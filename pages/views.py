from django.views.generic import TemplateView


# Create your views here.


class HomePageView(TemplateView):
    template_name = "todo_list.html"
