from django import forms

from CTRS_course_project.projection.models import Projection, Seat


class CreateProjectionForm(forms.ModelForm):
    class Meta:
        model = Projection
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy (DOB)',
                'class': 'form-control'
            }),
            'hour': forms.TimeInput(attrs={
                'type': 'time', 'placeholder': 'HH-MM (DOB)',
                'class': 'form-control'
            }),
        }

    def save(self, commit=True):
        projection = super().save(commit=commit)

        rows = projection.hall.rows
        seats_per_row = projection.hall.seats_per_row

        objs = []

        for row in range(1, rows + 1):
            for seat in range(1, seats_per_row + 1):
                objs.append(Seat(row_n=f"{row:02d}", seat_n=f"{seat:02d}", projection_id=projection.id))

        Seat.objects.bulk_create(objs)

        if commit:
            projection.save()

        return projection

