from webbrowser import get
from django.shortcuts import redirect, render
from petstragram.main_app.forms import ProfileForm

from petstragram.main_app.models import PetPhoto, Profile

def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

# Create your views here.
def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }

    return render(request, 'home_page.html', context)

def show_dashboard(request):
    profile = get_profile()
    if not profile:
        return redirect('401_error.html')

    pet_photos = set(PetPhoto.objects\
        .filter(tagged_pets__user_profile=profile))
    context = {
        'pet_photos': pet_photos,
    }

    return render(request, 'dashboard.html', context)

def show_profile(request):
    profile = get_profile()
    total_likes_count = sum(pp.likes for pp in PetPhoto.objects.filter(tagged_pets__user_profile=profile))
    total_images_count = len(PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
    context = {
        "profile": profile,
        "total_likes_count": total_likes_count,
        "total_images_count": total_images_count,
    }

    return render(request, 'profile_details.html', context)

def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects \
        .prefetch_related('tagged_pets') \
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo,
    }

    return render(request, 'photo_details.html', context)

def like_pet(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet photo details', pk)

def create_profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }


    return render(request, 'profile_create.html', context)

def edit_profile(request):
    return render(request, 'profile_edit.html')

def delete_profile(request):
    return render(request, 'profile_delete.html')

def create_pet(request):
    return render(request, 'pet_create.html')

def edit_pet(request):
    return render(request, 'pet_edit.html')

def delete_pet(request):
    return render(request, 'pet_delete.html')

def create_pet_photo(request):
    return render(request, 'photo_create.html')

def edit_pet_photo(request):
    return render(request, 'photo_edit.html')
