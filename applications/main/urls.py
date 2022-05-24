from django.urls import path

from applications.main.views import StudentListView

urlpatterns = [
    path('', StudentListView.as_view(), name='home-page'),
]