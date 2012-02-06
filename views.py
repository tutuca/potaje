from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from potaje.models import Section
from potaje.forms import EmailForm


def home(request):
    sections = Section.objects.all()
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
        'master.html',
        {
            'sections': sections,
            'form':form
        }
    )

def contact(request,*args,**kwargs):


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
