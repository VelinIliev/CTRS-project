from django import forms

from CTRS_course_project.movies.models import Movie, MovieComment, MovieVotes


class CreateMovieForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Movie
        exclude = ('rating', 'votes',)
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


class EditMovieForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Movie
        # fields = '__all__'
        exclude = ('rating', 'votes',)


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
        fields = ('rating',)
        widgets = {
            'rating': forms.NumberInput(
                attrs={
                    'min': '0',
                    'max': '10',
                },
            )
        }
