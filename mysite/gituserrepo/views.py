from django.http import HttpResponse
from django.template import loader
from django.apps import apps
from django.shortcuts import get_object_or_404, render
from .models import User
import json , requests

def index(request):
    users_list = User.objects.order_by('-pub_date')[:5]
    template = loader.get_template('gituserrepo/index.html')
    context = {
        'users_list': users_list,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    details_of_users = get_object_or_404(User,pk=id)
    template = loader.get_template('gituserrepo/details.html')
    context = {
        'details_of_users': details_of_users,
    }
    return HttpResponse(template.render(context, request))

def repolist(request, id):
    details_of_users = get_object_or_404(User,pk=id)
    template = loader.get_template('gituserrepo/repolist.html')
    context = {
        'details_of_users': details_of_users,
    }
    r = requests.get('https://api.github.com/users/%s/repos' % details_of_users.git_user_name)
    content = r.text
    return HttpResponse(content)
    #return HttpResponse("Show the list of repo for %s" % )