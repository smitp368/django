from django import forms
from .models import STUDENT
#DataFlair
class StudentCreate(forms.ModelForm):
    class Meta:
        model = STUDENT
        fields = '__all__'