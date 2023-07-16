import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import F
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic as views

from CTRS_course_project.movies.forms import CreateMovieForm, CommentForm, VoteForm
from CTRS_course_project.movies.helpers import calculate_runtime, calculate_rating, find_vote
from CTRS_course_project.movies.models import Movie, MovieComment, MovieVotes
from CTRS_course_project.projection.models import Projection


class CreateMovieView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    permission_required = 'movies.add_movie'
    login_url = "/profile/login/"
    template_name = 'movies/movie-create-page.html'
    form_class = CreateMovieForm

    def get_success_url(self):
        return reverse_lazy('details movie', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class DisplayMovieDetailsView(views.View):

    def get(self, request, pk, slug):
        movie = Movie.objects.filter(pk=pk, slug=slug).get()
        comment_form = CommentForm()

        comments = MovieComment.objects.filter(movie_id=pk).order_by('publication_date_and_time')
        updated_comments = comments.annotate(
            updated_datetime=F('publication_date_and_time') + timezone.timedelta(hours=3)
        )
        votes = MovieVotes.objects.filter(movie=movie).count()
        today = datetime.datetime.today().date()
        context = {
            'movie': movie,
            'comment_form': comment_form,
            'writers': movie.writers.split(", "),
            'directors': movie.directors.split(", "),
            'actors': movie.actors.split(", "),
            'runtime': calculate_runtime(movie.runtime),
            'rating': movie.rating,
            'votes': votes,
            'comments': updated_comments,
            'logged_user': self.request.user.is_authenticated,
            'projections': Projection.objects.filter(movie=movie, date__gte=today).order_by('date', 'hour')
        }

        return render(request, 'movies/movie-details-page.html', context)

    def post(self, request, pk, slug):
        movie = Movie.objects.filter(pk=pk, slug=slug).get()

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = self.request.user
            comment.save()
            return redirect('{}#comments'.format(reverse('details movie', kwargs={'pk': pk, 'slug': slug})))

        else:
            return redirect('index')


class DisplayMoviesView(views.ListView):
    template_name = 'movies/movies-main-page.html'
    model = Movie
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        rating = self.request.GET.get('rating', '')

        if search and rating:
            queryset = queryset.filter(title__icontains=search, is_active=1).order_by('-rating')
        elif search:
            queryset = queryset.filter(title__icontains=search, is_active=1).order_by('-pk')
        elif rating == 'dsc':
            queryset = queryset.filter(is_active=1).order_by('-rating')
        else:
            queryset = Movie.objects.filter(is_active=1).order_by('-pk')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['rating'] = self.request.GET.get('rating', '')
        return context


class EditMovieView(LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    permission_required = 'movies.change_movie'
    login_url = "/profile/login/"
    template_name = 'movies/movie-edit-page.html'
    model = Movie
    fields = ('title', 'year', 'image', 'runtime', 'plot', 'directors', 'writers', 'actors', 'genres', 'country',
              'languages', 'contentRating', 'imbd_link', 'is_active')

    def get_success_url(self):
        return reverse_lazy('details movie', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class VoteMovieView(LoginRequiredMixin, views.View):
    login_url = "/profile/login/"
    template_name = 'movies/movie-vote-page.html'
    model = MovieVotes
    fields = '__all__'

    def get(self, request, pk, slug):
        movie = Movie.objects.filter(pk=pk, slug=slug).get()

        user = self.request.user
        vote_form = VoteForm()
        user_rating = find_vote(movie, user)

        context = {
            'movie': movie,
            'user': self.request.user,
            'form': vote_form,
            'already_voted': user_rating,
        }
        return render(request, 'movies/movie-vote-page.html', context)

    def post(self, request, pk, slug):
        movie = Movie.objects.filter(pk=pk, slug=slug).get()

        user = self.request.user
        vote_form = VoteForm(request.POST)

        if vote_form.is_valid():
            vote = vote_form.save(commit=False)
            vote.movie = movie
            vote.user = self.request.user
            vote.save()

            movie.rating = calculate_rating(movie)
            movie.votes = MovieVotes.objects.filter(movie=movie).count()
            movie.save()

            return redirect(reverse('details movie', kwargs={'pk': pk, 'slug': slug}))
        else:
            context = {
                'movie': movie,
                'user': user,
                'form': vote_form,
                'already_voted': find_vote(movie, user),
            }
            return render(request, 'movies/movie-vote-page.html', context)
