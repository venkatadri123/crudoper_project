from django import forms
from app_crudoper.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class ImageUploadForm(forms.Form):
    profile_photo = forms.ImageField(allow_empty_file=True)
