from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course
# Create your views here.

def course_view(request):
    course_list = Course.objects.all()
    course_dictionary = {'course': course_list}
    return render(request, 'courses/index.html', context=course_dictionary)

def course_detail(request, pk):
    course = Course.objects.get(pk = pk)
    course_dict = {'course':course}
    return render(request, 'courses/course_detail.html', context=course_dict)