from django.contrib import admin
from django.urls import path
from student.views import student_list, student_create, student_update, student_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', student_list, name='student_list'),
    path('',student_create, name='student_create'),
    path('<int:pk>/edit/',student_update, name='student_update'),
    path('<int:pk>/delete/',student_delete, name='student_delete'),
    
]