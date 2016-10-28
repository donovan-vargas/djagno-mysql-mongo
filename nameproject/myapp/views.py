from django.shortcuts import render
from .models import grades

def get_grades(request):
    my_grades = grades.objects()
    context = {
        'my_grades': my_grades
    }
    return render(request, 'myapp/get_grades.html', context)
