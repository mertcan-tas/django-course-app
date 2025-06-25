from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

db = {
    "categories": [
        {"id": 1, "name": "Programlama", "slug": "programlama"},
        {"id": 2, "name": "Yapay Zeka", "slug": "yapay-zeka"},
        {"id": 3, "name": "Mobil", "slug": "mobil"},
    ],
    "courses": [
        {
            "title": "Tüm Yönleriyle MySql 8 ve Veri Tabanı Programlama",
            "description": "MySQL 8 ve veri tabanı programlama konusunda kapsamlı bir eğitim.",
            "imageUrl": "1.webp",
            "slug": "mysql-8-veri-tabani-programlama",
            "date": "2025-10-10",
            "category_id": 1,
            "isActive": True,
            "isUpdated": True
        },
        {
            "title": "Sıfırdan Uygulamalı React Geliştirme: Hooks,Redux & Firebase",
            "description": "React, Hooks, Redux ve Firebase kullanarak sıfırdan uygulamalı geliştirme öğrenin.",
            "imageUrl": "2.webp",
            "slug": "sifirdan-uygulamali-react-gelistirme",
            "date": "2025-10-10",
            "category_id": 1,
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "Python ile Yapay Zeka",
            "description": "Python kullanarak yapay zeka öğrenin.",
            "imageUrl": "3.webp",
            "slug": "python-ile-yapay-zeka",
            "date": "2025-11-01",
            "category_id": 2,
            "isActive": False,
            "isUpdated": True
        },
    ]
}

def index(request):
    categories = db["categories"]
    courses = db["courses"]
    return render(request, "courses/index.html", {
        "categories": categories,
        "courses": courses
    })
    
def courseList(request):
    courses = db["courses"]
    return render(request, "courses/courseList.html", {
        "courses": courses
    })

def details(request, course_slug):
    course = next((c for c in db["courses"] if c["slug"] == course_slug), None)
    if course:
        return render(request, "courses/details.html", {
            "course": course
        })
    return HttpResponseNotFound("Kurs bulunamadı.")

def getCoursesByCategory(request, category_slug):
    selected_category = next((c for c in db["categories"] if c["slug"] == category_slug), None)
    if selected_category:
        category_id = selected_category["id"]
        courses_in_category = [c for c in db["courses"] if c["category_id"] == category_id]
        return render(request, "courses/courses.html", {
            'category': selected_category,
            'courses': courses_in_category,
        })
    return HttpResponseNotFound("Kategori bulunamadı.")

def getCoursesByCategoryId(request, category_id):
    selected_category = next((c for c in db["categories"] if c["id"] == category_id), None)
    if selected_category:
        redirect_url = reverse('courses_by_category', args=[selected_category["slug"]])
        return redirect(redirect_url)
    return HttpResponseNotFound("Kategori bulunamadı.")