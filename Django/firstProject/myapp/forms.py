from django import forms
from .models import Logger

shifts = (
    (1,"moning"),
    (2,"night")
)
class demoForm (forms.Form):
    name = forms.CharField(max_length=20, required=False)
    email = forms.EmailField( help_text="Enter correct field")
    time = forms.TimeField()
    shits = forms.ChoiceField( widget=forms.RadioSelect,choices=shifts)

class Model_Form(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'