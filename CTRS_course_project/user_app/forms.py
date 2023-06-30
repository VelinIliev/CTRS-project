from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth.models import Group

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'age')
        field_classes = {'username': auth_forms.UsernameField}


class UserCreateStaffForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all())

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password', 'groups')

        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        user.is_staff = True
        if commit:
            user.save()
            user.groups.set(self.cleaned_data['groups'])
        return user


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {"username": auth_forms.UsernameField}
