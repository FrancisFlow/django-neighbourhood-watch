from django.shortcuts import render, redirect
from .forms import NewUserForm, NeighbourHoodForm, UpdateProfileForm
from .models import Profile, NeighbourHood, Business
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    current_user = request.user
    neighbourhoods=NeighbourHood.objects.all().order_by('-id')
    return render(request, 'home.html', {'neighbourhoods':neighbourhoods, 'current_user':current_user})


def register_request(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "User registration successful.")
            return redirect("/login")
        messages.error(request, "User registration failed. Invalid information")
    form=NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect("/")

            else:
                messages.error(request, "Invalid username or password.")
            
        else:
            messages.error(request, "Invalid username or password.")
    form=AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")

    # end authenticate request


#profile functions

@login_required()
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "profile.html", {"profile": profile, })



def update_profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():

            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')

    return render(request, 'update_profile.html', {"form": form})


@login_required(login_url='/login/')
def create_neighbourhood(request):
    current_user=request.user
    if request.method=="POST":
        neighbourhood_form=NeighbourHoodForm(request.POST, request.FILES)
        if neighbourhood_form.is_valid():
            neighbourhood=neighbourhood_form.save(commit=False)
            neighbourhood.user=current_user
            neighbourhood.save()
        return redirect('home')
    else:
        neighbourhood_form=NeighbourHoodForm()
    params= {'neighbourhood_form':neighbourhood_form}
    return render(request, 'create_neighbourhood.html', params)
