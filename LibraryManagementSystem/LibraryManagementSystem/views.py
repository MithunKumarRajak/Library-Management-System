from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'handler404.html')


def send_test_email(request):
    send_mail(
        subject='Hello from Django',
        message='This is a test email sent using Django.',
        from_email=None,  # uses DEFAULT_FROM_EMAIL
        recipient_list=['test@example.com'],
        fail_silently=False,
    )
    return HttpResponse("Email Sent Successfully!")
