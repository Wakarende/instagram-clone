from django.shortcuts import render,redirect
from .models import Image,Profile
from
# Create your views here.
def home(request):
  return render(request, 'home.html')

def create_profile(request):
  current_user = request.user
  if request.method == 'POST':
    form = CreateProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      profile.save()
        # return redirect(home)
    return HttpResponseRedirect('/')

  else:
    form = CreateProfileForm()
  return render(request, 'create-profile.html', {"form": form})