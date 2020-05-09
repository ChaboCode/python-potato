from django.urls import path
from . import views
from . import teacher_views

urlpatterns = [
    path('', views.hello_nerv, name='hello_nerv'),
    path('teacher/getGroups/', teacher_views.getGroups),
    path('students/', views.getAllStudents),
]
