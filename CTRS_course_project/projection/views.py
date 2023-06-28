import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from CTRS_course_project.projection.forms import CreateProjectionForm
from CTRS_course_project.projection.helpers import get_seats, get_today_movies, get_days
from CTRS_course_project.projection.models import Projection, Seat


class DisplayProjectionView(views.ListView):
    template_name = 'projections/display-projections-page.html'
    model = Projection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = get_days()[0]
        context['date'] = today
        context['days'] = get_days()
        context['current_day'] = get_today_movies(today)
        context['current_day_date'] = str(today)
        return context


class DisplayProjectionByDayView(views.ListView):
    template_name = 'projections/display-projections-by-day.html'
    model = Projection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.strptime(self.kwargs['day'], "%Y-%m-%d").date()
        context['days'] = get_days()
        context['current_day'] = get_today_movies(self.kwargs['day'])
        context['current_day_date'] = self.kwargs['day']
        return context


class CreateProjectionView(LoginRequiredMixin, views.CreateView):
    login_url = "/profile/login/"
    template_name = 'projections/create-projection-page.html'
    form_class = CreateProjectionForm
    success_url = reverse_lazy('projection index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class DetailsProjectionView(LoginRequiredMixin, views.DetailView):
    template_name = 'projections/details-projection-view.html'
    model = Projection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seats'] = get_seats(self.object)
        context['free_seats'] = Seat.objects.filter(projection_id=self.object.id, is_taken=0).count()
        return context

#
# def reservations(request):
#     if request.method == "POST":
#         if request.POST.get("type") != "":
#             seat_pks = [int(x) for x in request.POST.get("type").split(", ")]
#             [Seat.objects.filter(pk=pk).update(is_taken=True) for pk in seat_pks]
#         return redirect('projection index')
#     return redirect('index')
