from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings

from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        if request.method == "POST" and request.is_ajax():
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = "New Enquiry: " + form.cleaned_data['subject']
                message = form.cleaned_data['message']
                from_email = form.cleaned_data['from_email']
                from_name = "Name: " + form.cleaned_data['from_name']
                body = from_name + " " + "Email: " + from_email + " " + message
                try:
                    send_mail(subject, body, from_email, ['nate@natemoore.me'])
                except BadHeaderError:
                    return HttpResponse('Bad header')
                return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=400)
    return render(request, 'contact/contact.html', {'form': form})
