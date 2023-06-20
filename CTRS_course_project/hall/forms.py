from django import forms

from CTRS_course_project.hall.models import Hall


class CreateHallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'
