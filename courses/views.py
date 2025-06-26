from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from courses.models import Course, Category

def index(request):
    courses_list = Course.objects.filter(is_active=True)
    paginator = Paginator(courses_list, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "courses/index.html", {
        "page_obj": page_obj,
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, "courses/details.html", {
        "course": course
    })
    
def getCoursesByCategory(request, slug):
    category = get_object_or_404(Category, slug=slug)
    course_list = category.courses.filter(is_active=True)  
    
    paginator = Paginator(course_list, 6)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "courses/category.html", {
        "page_obj": page_obj,
        "category": category,
    })