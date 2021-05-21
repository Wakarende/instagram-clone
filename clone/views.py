from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
  title= "Instagram"
  current_user =request.user

  timeline_images = []
  current_images = Image.objects.filter(profile = logged_in)
  for current_image in current_images:
    timeline_images.append(current_image.id)
  
  display_images= Image.objects.filter(pk__in = timeline_images).order_by('-post_date')
  liked = False
  for i in display_images:
    image = Image.objects.get(pk=i.id)
    liked = False
    if image.likes.filter(id =request.user.id).exists():
      liked = True

  return render(request, 'home.html', {"images":display_images,"liked":liked, "comments":comments, "title":title, "loggedIn":logged_in} )

@login_required(login_url='/accounts/login/')
def upload_image(request):
  title = "Instagram | Upload image"
  current_user = request.user
  try:
    profile = Profile.objects.get(user = current_user)
  except Profile.DoesNotExist:
    raise Http404()
  if request.method == "POST":
    form = UploadImageForm(request.POST, request.FILES)
  if form.is_valid():
    image = form.save(commit=False)
    image.profile = profile
    image.save()
    return redirect('home')
  else:
    form = UploadImageForm()
  return render(request, 'upload_image.html', {"form": form, "title": title})

# def create_profile(request):
#   current_user = request.user
#   if request.method == 'POST':
#     form = CreateProfileForm(request.POST, request.FILES)
#     if form.is_valid():
#       profile = form.save(commit=False)
#       profile.user = current_user
#       profile.save()
#         # return redirect(home)
#     return HttpResponseRedirect('/')

#   else:
#     form = CreateProfileForm()
#   return render(request, 'create-profile.html', {"form": form})


