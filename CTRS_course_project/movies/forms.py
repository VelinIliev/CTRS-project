from django import forms

from CTRS_course_project.movies.models import Movie, MovieComment, MovieVotes


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['rating', 'votes', 'temp_img', 'stars']
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
        widgets = {
            'text': forms.Textarea()
        }


class VoteForm(forms.ModelForm):
    class Meta:
        model = MovieVotes
        fields = ('rating', )
        widgets = {
            'rating': forms.NumberInput(
                attrs={
                    'min': '0',
                    'max': '10',
                },
            )
        }
