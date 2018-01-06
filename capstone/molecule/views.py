from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, Group

# Create your views here.

# render the login page
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('molecule:redirect_profile'))
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
        profile = UserProfile(user=user)                # red user is from the models and white user is in this scope
        profile.save()
        group = Group(name='default', user=user)                                 # name variable and referencing a Class
        group.save()
        return HttpResponseRedirect(reverse('molecule:profile'))
    return render(request, 'molecule/create_account.html')
    # return HttpResponse('create account')


@login_required
def redirect_profile(request):
    return HttpResponseRedirect(reverse('molecule:profile', args=[request.user.username]))    # key is string, value is contents of the variable
    # return HttpResponse('profile page')


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)             # request.user is the currently logged in user
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'molecule/profile.html', {'profile':profile, 'viewed_user':user})    # key is string, value is contents of the variable
    # return HttpResponse('profile page')


@login_required
def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    messages = {}
    if request.method == 'POST':
        if 'password' in request.POST:
            if request.POST['password'] == request.POST['verify_password']:
                request.user.set_password(request.POST['password'])
                messages['password'] = 'password changed!'
            else:
                messages['password'] = 'passwords do not match'
        else:
            request.user.first_name = request.POST['first_name']
            request.user.last_name = request.POST['last_name']
            request.user.email = request.POST['email']
            profile.bio = request.POST['bio']
            request.user.save()
            profile.save()
            messages['profile'] = 'profile updated'


    return render(request, 'molecule/edit_profile.html', {'profile':profile, 'messages':messages})
    # return HttpResponse('edit profile')


@login_required
def groups(request):                # the name of this link is "contacts"
    if request.method == 'POST':
        new_group = Group(name=request.POST['group_name'], user=request.user)   # create new group
        new_group.save()

    groups = Group.objects.filter(user=request.user)
    return render(request, 'molecule/groups.html', {'groups': groups})
    # return HttpResponse('manage groups')


@login_required
def add_contact(request, username):
    new_contact = get_object_or_404(User, username=username)
    group = get_object_or_404(Group, user=request.user, name='default')
    group.contacts.add(new_contact)
    group.save()

    return HttpResponseRedirect(reverse('molecule:groups'))


@login_required
def messages(request):
    return render(request, 'molecule/messages.html')
    # return HttpResponse('chat')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('molecule:index'))



