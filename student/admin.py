from django.contrib import admin
from .models import Student
from .utils import predict_course
from datetime import date

def calculate_age(birthdate):
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth', 'age', 'gender', 'interest', 'course')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('gender', 'course')
    ordering = ('last_name',)

    def save_model(self, request, obj, form, change):
    
        obj.age = calculate_age(obj.date_of_birth)
        obj.course = predict_course(obj.age, obj.gender, obj.interest)
        super().save_model(request, obj, form, change)