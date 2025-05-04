from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect  
from student.views import student_list, student_create, student_update, student_delete

def root_redirect(request):
    return redirect('student_list')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_redirect),  
    path('students/', student_list, name='student_list'),
    path('new/', student_create, name='student_create'),
    path('<int:pk>/edit/', student_update, name='student_update'),
    path('<int:pk>/delete/', student_delete, name='student_delete'),
]