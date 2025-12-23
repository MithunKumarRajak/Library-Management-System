from django.shortcuts import render
from .models import Message
from .forms import MessageForm, MessageModelForm

# 🔹 1. HTML Form – Manual Handling


def message_manual(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Message.objects.create(
            name=name,
            email=email,
            message=message
        )
        return render(request, 'home/success.html')

    return render(request, 'home/message_manual.html')


# 🔹 2. Django Form (forms.Form)
def message_form(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return render(request, 'home/success.html')
    else:
        form = MessageForm()

    return render(request, 'home/message_form.html', {'form': form})


# 🔹 3. ModelForm (forms.ModelForm)
def message_modelform(request):
    if request.method == "POST":
        form = MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/success.html')
    else:
        form = MessageModelForm()

    return render(request, 'home/message_modelform.html', {'form': form})


def home(request):
    return message_form(request)
