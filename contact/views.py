""" Imports required """
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from profiles.models import UserProfile
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    if request.method == "POST":
        # If POST, get info from form
        form_data = {
            'first_name': request.POST['first_name'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'order_number': request.POST['order_number'],
            'enquiry': request.POST['enquiry'],
        }
        contact_form = ContactForm(form_data)

        if contact_form.is_valid():
            messages.success(
                request, 'Enquiry sent!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Error sending enquiry. Try again.')
            return redirect(reverse('contact'))

    else:
        if request.user.is_authenticated:
            # If user is logged in try and prefill form with saved
            # information if available
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
        template = 'contact/contact.html'
        context = {
            'contact_form': contact_form
        }
        return render(request, template, context)