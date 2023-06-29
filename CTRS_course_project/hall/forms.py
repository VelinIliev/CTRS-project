from django import forms

from CTRS_course_project.hall.models import Hall


class CreateHallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ('name', 'rows', 'seats_per_row', 'description', 'image_url')
