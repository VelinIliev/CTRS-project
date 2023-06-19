from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

UserModel = get_user_model()


def index(request):
    context = {
        'users': UserModel.objects.all()
    }
    return render(request, 'common/index.html', context)
