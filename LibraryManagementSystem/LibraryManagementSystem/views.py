import os
from django.core.mail  import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings 

def handler404(request, exception):
    return render(request, 'handler404.html')

# Creating a simple view to test email sending functionality


def send_test_email(request):
    email=EmailMessage(
        subject='Hello from Django',
        body='This is a test email sent using Django.',
        from_email=None,  # uses DEFAULT_FROM_EMAIL from settings.py or the EMAIL_HOST_USER
        to=['esmartshopoffical@gmail.com'],
        bcc=['mithunkumarrajak18plus@gmail.com'],
        cc=['singalkumar1210@gmail.com'],

    )
    file_path = os.path.join(settings.MEDIA_ROOT, "pdf/resume.pdf")
    email.attach_file(file_path)
    email.send()
    return HttpResponse("Email Sent Successfully!")


def email_page(request):
    return render(request, 'email/send_email.html')
