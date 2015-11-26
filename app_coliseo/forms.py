from django import forms

from .models import MyModel
from .models import Persona

class MyModel(forms.ModelForm):

    class Meta:

        model = MyModel
        fields = ('title', )

class ModelPersona(forms.ModelForm):
	class Meta:
		model = Persona
		fields = '__all__'