from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from courses.models import Course, Category
from django.db.models import Q
from courses.forms import CourseCreateForm, CourseEditForm

def index(request):
    query = request.GET.get("search", "").strip()
    
    if query:
        courses_list = Course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query), is_active=True,)
    else:
        courses_list = Course.objects.filter(is_active=True)
    
    paginator = Paginator(courses_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "courses/index.html", {
        "page_obj": page_obj,
        "query": query,
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
    
def courseList(request):
    query = request.GET.get("search", "").strip()
    
    if query:
        courses_list = Course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query), is_active=True,)
    else:
        courses_list = Course.objects.filter(is_active=True)
    
    paginator = Paginator(courses_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "courses/course-list.html", {
        "page_obj": page_obj,
        "query": query,
    })


def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseCreateForm()
    return render(request, "courses/create-course.html", {"form": form})


def edit_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance=course)
        
        if form.is_valid():
            form.save()
            return redirect('course-list')
    else:
        form = CourseEditForm(instance=course)
    return render(request, "courses/edit-course.html", {"form": form, "slug": slug})

def delete_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == "POST":
        course.delete()
        return redirect('course-list')
    else:
        return render(request, "courses/delete-course.html", {"course": course})

    