from django import forms
from django.forms.fields import ChoiceField
from django.forms import TextInput
from ..models.item import *

class ItemRegisterForm(forms.ModelForm):

    class Meta():
        model=ItemModel    
        fields=('name', 'price', 'thumbnail_url', 'description')
        
        # テキストエリアのサイズ変更
        widgets = {
            'description': forms.Textarea(attrs={'rows':20, 'cols':40})
        }