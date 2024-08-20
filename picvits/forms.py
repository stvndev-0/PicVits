from django import forms
from .models import Picture

class PictureForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    class Meta:
        model = Picture
        fields = ['title', 'image']
        widget = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*', 'id': 'imageInput'})
        }