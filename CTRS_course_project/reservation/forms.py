from django import forms

from CTRS_course_project.reservation.models import Reservation


class CreateReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('projection',)
        exclude = '__all__'
