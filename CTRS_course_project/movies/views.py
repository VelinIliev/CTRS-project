from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from CTRS_course_project.movies.forms import CreateMovieForm, CommentForm
from CTRS_course_project.movies.helpers import calculate_runtime
from CTRS_course_project.movies.models import Movie, MovieComment


class CreateMovieView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
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


# class DisplayMovieDetailsView(views.DetailView):
#     template_name = 'movies/movie-details-page.html'
#     model = Movie
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['writers'] = self.object.writers.split(", ")
#         context['directors'] = self.object.directors.split(", ")
#         context['actors'] = self.object.actors.split(", ")
#         context['runtime'] = calculate_runtime(self.object.runtime)
#         context['is_staff'] = self.request.user.is_staff
#         return context

class DisplayMovieDetailsView(views.View):

    def get(self, request, pk, slug):
        movie = Movie.objects.filter(pk=pk).get()
        comment_form = CommentForm()
        context = {
            'movie': movie,
            'comment_form': comment_form,
            'writers': movie.writers.split(", "),
            'directors': movie.directors.split(", "),
            'actors': movie.actors.split(", "),
            'runtime': calculate_runtime(movie.runtime),
            'is_staff': self.request.user.is_staff,
            'comments': MovieComment.objects.filter(movie_id=pk),
            'logged_user': self.request.user.is_authenticated,
        }
        return render(request, 'movies/movie-details-page.html', context)

    def post(self, request, pk, slug):
        movie = Movie.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = self.request.user
            comment.save()
            return redirect('details movie', pk=pk, slug=slug)
        else:
            context = {
                'movie': movie,
                'comment_form': comment_form,
                'writers': movie.writers.split(", "),
                'directors': movie.directors.split(", "),
                'actors': movie.actors.split(", "),
                'runtime': calculate_runtime(movie.runtime),
                'is_staff': self.request.user.is_staff,
                'comments': MovieComment.objects.filter(movie_id=pk)
            }
            return render(request, 'movies/movie-details-page.html', context)


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
