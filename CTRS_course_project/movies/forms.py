from django import forms

from CTRS_course_project.movies.models import Movie, MovieComment


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'directors': forms.Textarea(
                attrs={
                    'placeholder': 'Enter the names separated by commas.',
                }),
            'actors': forms.Textarea(
                attrs={
                    'placeholder': 'Enter the names separated by commas.',
                }),
            'writers': forms.Textarea(
                attrs={
                    'placeholder': 'Enter the names separated by commas.',
                }),
            'genres': forms.Textarea(
                attrs={
                    'placeholder': 'Enter the names separated by commas.',
                }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('text',)