from webbrowser import get
from django.shortcuts import redirect, render
from petstragram.main_app.forms import ProfileForm, EditProfileForm, DeleteProfileForm, PetForm, EditPetForm, \
    DeletePetForm, PetPhotoForm, EditPetPhotoForm

from petstragram.main_app.models import PetPhoto, Profile, Pet


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
    pets = list(Pet.objects.filter(user_profile=profile))
    total_likes_count = sum(pp.likes for pp in PetPhoto.objects.filter(tagged_pets__user_profile=profile))
    total_images_count = len(PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
    context = {
        "profile": profile,
        "total_likes_count": total_likes_count,
        "total_images_count": total_images_count,
        "pets": pets,
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
    profile = get_profile()

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)

        context = {
            'form': form,
        }

    return render(request, 'profile_edit.html', context)

def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile_delete.html', context)

def create_pet(request):
    pet = Pet(user_profile=get_profile())

    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PetForm(instance=pet)

    context = {
        'form': form,
    }

    return render(request, 'pet_create.html', context)

def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditPetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pet_edit.html', context)

def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeletePetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = DeletePetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pet_delete.html', context)

def create_pet_photo(request):

    if request.method == 'POST':
        form = PetPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PetPhotoForm()

    context = {
        'form': form,
    }

    return render(request, 'photo_create.html', context)

def edit_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditPetPhotoForm(request.POST, request.FILES, instance=pet_photo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditPetPhotoForm(instance=pet_photo)

    context = {
        'form': form,
        'pet_photo': pet_photo,
    }

    return render(request, 'photo_edit.html', context)
