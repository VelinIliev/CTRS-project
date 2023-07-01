import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic as views

from CTRS_course_project.projection.helpers import get_seats
from CTRS_course_project.projection.models import Projection, Seat
from CTRS_course_project.reservation.forms import CreateReservationForm
from CTRS_course_project.reservation.models import Reservation
from CTRS_course_project.tickets.models import Ticket


@login_required
def create_reservation(request):
    projection_pk = int(request.GET.get('projection'))
    projection = Projection.objects.filter(pk=projection_pk).get()

    if request.method == "GET":
        form = CreateReservationForm()
    else:
        today = str(datetime.datetime.today().date())
        reservation = Reservation(
            projection=projection,
            date=today,
            user=request.user
        )
        reservation.save()
        return redirect('reservation step 1', pk=reservation.pk)

    context = {
        'projection': projection,
        'form': form,
        'seats': get_seats(projection),
        'free_seats': Seat.objects.filter(projection_id=projection.id, is_taken=0).count(),
    }
    return render(request, 'reservations/reservation-start-page.html', context)


class ReservationStep1View(LoginRequiredMixin, views.UpdateView):
    login_url = "/profile/login/"
    template_name = 'reservations/reservation-step1-page.html'
    model = Reservation
    fields = ('type_of_tickets', 'number_of_tickets', 'total_price',)

    def get_success_url(self):
        return reverse('reservation step 2', kwargs={'pk': self.object.id, })

    def get_context_data(self, **kwargs):
        projection = Projection.objects.filter(pk=self.object.projection.id).get()
        context = super().get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.all()
        context['weekdays'] = True if self.object.projection.date.weekday() < 5 else False
        context['free_seats'] = Seat.objects.filter(projection_id=projection.id, is_taken=0).count()
        return context


class ReservationStep2View(LoginRequiredMixin, views.UpdateView):
    login_url = "/profile/login/"
    template_name = 'reservations/reservation-step2-page.html'
    model = Reservation
    fields = ('reserved_seats', 'is_finished')

    def get_success_url(self):
        return reverse('reservation review', kwargs={'pk': self.object.id, })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projection = Projection.objects.filter(pk=self.object.projection.id).get()
        context['projection'] = projection
        context['seats'] = get_seats(projection)
        context['free_seats'] = Seat.objects.filter(projection_id=projection.id, is_taken=0).count()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        seats = [int(x) for x in self.request.POST.get("reserved_seats").split(", ")]
        [Seat.objects.filter(pk=pk).update(is_taken=True) for pk in seats]

        return super().post(request, *args, **kwargs)


class ReservationDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'reservations/reservation-review-page.html'
    model = Reservation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tickets = self.object.type_of_tickets.split(";")
        new_tickets = []
        for ticket in tickets:
            ticket = ticket.split(",")
            if len(ticket) > 1:
                ticket_type = ticket[0]
                number_of_tickets = int(ticket[1])
                ticket_price = float(ticket[2])
                ticket = f'{ticket_type} x {number_of_tickets} = {(ticket_price * number_of_tickets):.2f}'
                new_tickets.append(ticket)
        context['tickets'] = new_tickets
        seats = [int(x) for x in self.object.reserved_seats.split(", ")]
        seats = Seat.objects.filter(pk__in=seats)
        context['seats'] = seats
        context['is_owner'] = self.request.user == self.object.user
        return context
