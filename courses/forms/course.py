from django import forms
from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         max_length=50,
#         required=True,
#         error_messages={'required': "Lütfen başlık alanını doldurun!"},
#         widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'false'})
#     )
#     description = forms.CharField(
#         required=True,
#         widget=forms.Textarea(attrs={'class': 'form-control'})
#     )

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "image", "category")
        labels = {
            "title": "Başlık",
            "description": "İçerik"
        }
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            "category": forms.Select(attrs={'class': 'form-control', 'required': 'false'}),
        }
        error_messages = {
            "title": {
                "required": "Lütfen başlık alanını doldurun!",
                "max_length": "Maksimum 50 karakter girin!"
            }
        }
        
class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "image", "category")
        readonly_fields = ('slug',)
        labels = {
            "title": "Başlık",
            "description": "İçerik"
        }
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            "category": forms.Select(attrs={'class': 'form-control', 'required': 'false'}),
        }
        error_messages = {
            "title": {
                "required": "Lütfen başlık alanını doldurun!",
                "max_length": "Maksimum 50 karakter girin!"
            }
        }

