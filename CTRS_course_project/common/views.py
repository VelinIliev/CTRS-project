from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permissions'] = self.request.user.has_perm('user_app.view_user')
        context['permissions_hall'] = self.request.user.has_perm('hall.view_hall')
        # context['permissions_hall'] = self.request.user.has_perm('hall.edit_hall')
        return context


class AdminIndexView(LoginRequiredMixin, views.TemplateView):
    template_name = 'common/index-admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context
