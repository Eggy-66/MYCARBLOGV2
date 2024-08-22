from django import forms
from .models import Item, Message

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'year', 'power', 'fuel', 'cabin_type', 'description', 'price', 'phone_number', 'photo']



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
