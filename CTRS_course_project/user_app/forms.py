from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'age')
        field_classes = {'username': auth_forms.UsernameField}


class UserCreateStaffForm(UserCreateForm):
    def save(self, commit=True):
        user = super(UserCreateStaffForm, self).save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {"username": auth_forms.UsernameField}
