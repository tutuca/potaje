from django.shortcuts import render, redirect
from django.core.mail import send_mail
from potaje.models import Section, Album
from potaje.forms import EmailForm


def home(request):
    sections = Section.objects.select_related().all()
    form = EmailForm()
    return render(
        request,
        'master.html',
        {
            'sections': sections,
            'form': form
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
