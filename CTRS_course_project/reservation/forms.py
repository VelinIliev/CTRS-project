from django import forms

from CTRS_course_project.reservation.models import Reservation


#
class CreateReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('projection',)
        exclude = '__all__'
        # fields = ('projection', 'date')
        # widgets = {
        #     'projection': forms.SelectMultiple(
        #         attrs={
        #             'hid': 'Fruit Name',
        #         }),
        # }
        # widgets = {
        #     'projection': forms.HiddenInput(),
        #     'date': forms.HiddenInput(),
        # }
#
#
# class StepOneReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ('type_of_tickets', 'number_of_tickets', 'total_price', 'user', 'projection')
