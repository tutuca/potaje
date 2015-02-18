from django.shortcuts import render, redirect
from django.core.mail import send_mail
from albums.models import Album
from albums.forms import EmailForm
from profiles.models import Profile


def home(request):
    profiles = Profile.objects.select_related().all()
    return render(
        request,
        'master.html',
        {
            'profiles': profiles,
            'is_staff': request.user.is_staff
        }
    )


def album(request, id):
    album_object = Album.objects.get(pk=id)
    return render(
        request,
        'album.html',
        {'album': album_object}
    )


def about(request):
    return render(
        request,
        'about.html',
        {}
    )


def contact(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():

            send_mail(
                'Nuevo mensaje de nuestra web',
                form.data['message'],
                form.data['email'],
                [
                    'anacomes@gmail.com',
                ],
            )
            return redirect('/gracias/')

    return render(
        request,
        'contact.html',
        {
            'form': form,
            'section': 'contact',
        }
    )


def email_success(request):
    return render(request, 'email_success.html')
