from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from courses.models import Course, Category
from django.db.models import Q
from courses.forms import CourseCreateForm

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
    
    
def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)
        
        if form.is_valid():
            kurs = Course(title=form.cleaned_data["title"], description=form.cleaned_data["title"], category_id=Category.objects.first().id)
            kurs.save()
            return redirect('index')
    else:
        form = CourseCreateForm()
    return render(request, "courses/create-course.html", {"form": form})