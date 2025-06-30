from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        required=True,
        error_messages={'required': "Lütfen başlık alanını doldurun!"},
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'false'})
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
