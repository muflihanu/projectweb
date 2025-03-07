from django import forms
from .models import *


class User_signupform(forms.ModelForm):
    class Meta:
        model=Usersign_up
        fields=['username','password','email','phone']


class Userlogin(forms.ModelForm):
    class Meta:
        model=Usersign_up
        fields=['username','password']


class Vendorregistorform(forms.ModelForm):
    class Meta:
        model=Vendorregister
        fields=['businessname','businnesregistornumber','email','password','phone']       


class Vendorlogin(forms.ModelForm):
    class Meta:
        model=Vendorregister
        fields=['email','password']


class vpackageform(forms.ModelForm):
    class Meta:
        model=Packagecreate
        fields=['title','description','date','image','price']

class Bookingdetailsform(forms.ModelForm):
    class Meta:
        model=Bookingdetails
        fields=['fullname','package','number_of_people','booking_date','phone']