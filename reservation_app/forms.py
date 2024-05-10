from django import forms
from reservation_app.models import Sala
class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['name', 'capacity', 'projector_availability']

class ModifySalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['name', 'capacity', 'projector_availability']

class ReserveSalaForm(forms.Form):
    komentarz = forms.CharField(widget=forms.Textarea)
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))