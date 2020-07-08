from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        '''This is just a class container with some options 
        (metadata) attached to the model. It defines such things as 
        available permissions, associated database table name, whether 
        the model is abstract or not, 
        singular and plural versions of the name etc.'''
        #Nkit rast i paraqet cilat vlera pi dojna ne form
        #Edhe me cilin model mu merr
        #ktu ruhen pra configurations me ni ven
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["image"]