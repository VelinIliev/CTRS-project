from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from CTRS_course_project.movies.forms import CreateMovieForm
from CTRS_course_project.movies.helpers import calculate_runtime
from CTRS_course_project.movies.models import Movie


class CreateMovieView(LoginRequiredMixin, PermissionRequiredMixin,  views.CreateView):
    permission_required = 'movies.add_movie'
    login_url = "/profile/login/"
    template_name = 'movies/movie-create-page.html'
    form_class = CreateMovieForm

    def get_success_url(self):
        return reverse_lazy('details movie', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

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
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(title__icontains=search, is_active=1).order_by('-pk')
        else:
            queryset = Movie.objects.filter(is_active=1).order_by('-pk')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class EditMovieView(LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    permission_required = 'movies.change_movie'
    login_url = "/profile/login/"
    template_name = 'movies/movie-edit-page.html'
    model = Movie
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('details movie', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context
