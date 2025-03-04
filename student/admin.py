from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','age', 'date_of_birth', 'gender')
    search_fields = ('first_name', 'last_name', 'email')

