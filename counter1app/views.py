
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Add_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import SignUpForm,Add_userForm,EditSupervisor
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import (DetailView)
from django.contrib.auth import authenticate,login




# Create your views here.

def index(request):
    users = Add_user.objects.filter()
    return render(request,'index.html',{'users':users})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

def create_user(request):
    '''
    View function to add a new supervisor
    '''
    if request.method == 'POST':
        form = Add_userForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)

            '''
            above line of code displays a user registered in a specific sacco or orgamisation by counter1
            '''
            user.save()
            messages.success(request, f'Congratulations! You have succesfully Added a new User!')
            return redirect('/')
    else:
        form = Add_userForm()
    return render(request, 'create_user.html', {"form": form})




def edit_superlist(request, supervisor_id):
    '''
    View function to edit an instance of a supervisor/user already created by the admin
    '''
    supervisor = Add_user.objects.get(pk=supervisor_id)
    if request.method == 'POST':
        form = EditSupervisor(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success! Your edit has been successful!')
            return redirect('/')
    else:
        form = EditSupervisor(instance=supervisor)
    return render(request, 'edit_user.html', {"form": form, "supervisor":supervisor})
