from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from courses.models import Course, Category

def index(request):
    courses = Course.objects.filter(is_active=1)
    return render(request, "courses/index.html", {
        "courses": courses
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, "courses/details.html", {
        "course": course
    })

def getCoursesByCategory(request, slug):
    courses = get_object_or_404(Category, slug=slug).courses.all()
    return render(request, "courses/category.html", {
        'courses': courses,
    })
