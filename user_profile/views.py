from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from user_profile.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def about(request):
    return render(request, 'about.html')
#
# def my_profile(request):
#     # profile = get_object_or_404(Profile, slug=slug)
#     # context = { 'profile': profile }
#     return render(request, 'user_profile/my_profile.html')
@login_required(login_url='login')
def home(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'home.html', context={'userinfo': profile })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.f_name = form.cleaned_data.get('f_name')
            user.profile.l_name = form.cleaned_data.get('l_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.github_profile = form.cleaned_data.get('github_profile')
            user.profile.reddit_profile = form.cleaned_data.get('reddit_profile')
            user.profile.facebook_profile = form.cleaned_data.get('facebook_profile')
            user.profile.linkedin_profile = form.cleaned_data.get('linkedin_profile')
            user.profile.image = form.cleaned_data.get('image')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
