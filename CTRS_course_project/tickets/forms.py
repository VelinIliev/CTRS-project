from django import forms

from CTRS_course_project.tickets.models import Ticket


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


class ListTickerForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


class EditTickerForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
