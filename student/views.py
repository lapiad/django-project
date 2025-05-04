from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from .utils import predict_course  # Make sure you have this function

def student_list(request):
    students = Student.objects.all()  # Get all students
    return render(request, 'students/student_list.html', {'students': students})  # Corrected context key

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.course = predict_course(student.age, student.gender, student.interest)  # Predict the course
            student.save()
            messages.success(request, 'Student added successfully with predicted course.')  # Success message
            return redirect('student_list')  # Redirect to the student list after creation
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})  # Render the form

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)  # Get student object based on primary key
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.course = predict_course(student.age, student.gender, student.interest)  # Predict the course
            student.save()
            messages.success(request, 'Student updated successfully.')  # Success message
            return redirect('student_list')  # Redirect to the student list after update
    else:
        form = StudentForm(instance=student)  # Pre-fill the form with existing student data
    return render(request, 'students/student_form.html', {'form': form})  # Render the form

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)  # Get student object based on primary key
    if request.method == 'POST':
        student.delete()  # Delete the student
        messages.success(request, 'Student deleted successfully.')  # Success message
        return redirect('student_list')  # Redirect to the student list after deletion
    return render(request, 'students/student_confirm_delete.html', {'student': student})  # Render delete confirmation template