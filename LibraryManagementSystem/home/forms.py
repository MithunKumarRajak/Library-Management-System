from django import forms
from django.forms import ModelForm
from .models import Message

# 🔹 Django Form (forms.Form)
class MessageForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# 🔹 ModelForm (forms.ModelForm)
class MessageModelForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
