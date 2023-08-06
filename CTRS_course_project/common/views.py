from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'common/index.html'


class AdminIndexView(LoginRequiredMixin, views.TemplateView):
    template_name = 'common/index-admin.html'
