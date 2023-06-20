from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic as views

from CTRS_course_project.movies.forms import CreateMovieForm, DisplayMovieForm, EditMovieForm
from CTRS_course_project.movies.helpers import calculate_runtime
from CTRS_course_project.movies.models import Movie


def index(request):
    return HttpResponse("index movies")


class CreateMovieView(LoginRequiredMixin, views.CreateView):
    login_url = "/profile/login/"
    template_name = 'movies/movie-create-page.html'
    form_class = CreateMovieForm

    # success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy('details movie', kwargs={'pk': self.object.pk, })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class DisplayMovieDetailsView(views.DetailView):
    template_name = 'movies/movie-details-page.html'
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['writers'] = self.object.writers.split(", ")
        context['directors'] = self.object.directors.split(", ")
        context['actors'] = self.object.actors.split(", ")
        context['runtime'] = calculate_runtime(self.object.runtime)
        context['is_staff'] = self.request.user.is_staff
        return context


class DisplayMoviesView(views.ListView):
    template_name = 'movies/movies-main-page.html'
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all().order_by('-id')[:5]
        return context


class EditMovieView(LoginRequiredMixin, views.UpdateView):
    login_url = "/profile/login/"
    template_name = 'movies/movie-edit-page.html'
    model = Movie
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('details movie', kwargs={'pk': self.object.pk, })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context
