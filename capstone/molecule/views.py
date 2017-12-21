from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# render the login page
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('molecule:profile'))
        else:
            print('login unsuccessful')
            return render(request, 'molecule/index.html', {'error_message': 'username/password not found'})
    return render(request, 'molecule/index.html')


def create_account(request):
    if request.method =='POST':
        username = request.POST['username']             # these need to match the names exactly from the create_account.html file
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return HttpResponseRedirect(reverse('molecule:profile'))
    return render(request, 'molecule/create_account.html')
    # return HttpResponse('create account')


@login_required
def profile(request):
    return render(request, 'molecule/profile.html')
    # return HttpResponse('profile page')


@login_required
def edit_profile(request):
    return render(request, 'molecule/edit_profile.html')
    # return HttpResponse('edit profile')


@login_required
def groups(request):
    return render(request, 'molecule/groups.html')
    # return HttpResponse('manage groups')


@login_required
def messages(request):
    return render(request, 'molecule/messages.html')
    # return HttpResponse('chat')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('molecule:index'))



