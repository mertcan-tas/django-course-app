from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)