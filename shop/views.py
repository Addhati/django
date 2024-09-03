from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course, Category


# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def course(request, course_id):
    # Option 1
    # try:
    #     course = Course.objects.get(id=course_id)
    #     return render(request, 'course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404("Course does not exist")

    # Option 2
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course.html', {'course': course})
