from django.shortcuts import render
from .forms import MessageForm
from .models import Message
# Create your views here.


def message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(  # for the saveing the message
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'])
            return render(request, 'home/success.html')
    else:
        form = MessageForm()
    return render(request, 'home/message.html', {'form': form})
