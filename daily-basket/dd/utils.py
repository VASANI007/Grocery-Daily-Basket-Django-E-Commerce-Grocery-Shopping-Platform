from django.conf import settings
from django.core.mail import *
from django.shortcuts import redirect, render



def send_email_to_client(request):
    name = request.POST.get("cname")
    subject = request.POST.get("csubject")
    message = request.POST.get("cmsg")
    from_email = settings.EMAIL_HOST_USER
    recipient_list = request.POST.get("cemail")
    send_mail(name, subject, message, from_email, recipient_list)
    return render(request,'contact.html')