from django.views.generic import ListView
from applications.main.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'home_page.html'
    context_object_name = 'students'



