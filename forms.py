import re
from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class signupForm(forms.Form):
    #userName
    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=32,placeholder="Eg: john345")), label="Username")
    #emailID of the user
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=75,placeholder="Eg: john@yahoo.com")), label="Email address", initial='example@abc.com')
    #password of user
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False,placeholder="john345")), label= "Password")
    #renter the password
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False,placeholder="john345")), label= "Password (again)")
    #choices to register/login as an ngo or user
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=(('1','NGO',),('2','Member',)),label = 'Type of User')

    def clean_email(self):
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError( "There is already an account on this email-ID")

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError( "The two password fields did not match.")

        return self.cleaned_data
    
class commonUserRegistration(forms.Form):
    #first name of common user
    firstName = forms.RegexField(regex = r'^\w+$', widget = forms.TextInput(attrs = dict(required=True, max_length = 32)), label = "First Name")
    #last name of user
    lastName = forms.RegexField(regex = r'^\w+$', widget = forms.TextInput(attrs = dict(required=True, max_length = 32)), label = "Last Name")
    #contact number of user
    contactNumber = forms.IntegerField(widget=forms.TextInput(attrs = dict(required=True, max_length = 10)), label = "Conact Number")
    #address of user
    address = forms.CharField(widget = forms.TextInput(attrs = dict(required=True, max_length = 100)), label = "Contact Address")
    #profession of user
    profession = forms.ChoiceField(widget = forms.RadioSelect, choices = (('1','Student'),('2','Professional')), label= "Your Profession" )
    #dob of user
    dob = forms.DateField(widget=forms.TextInput(attrs=dict(required=True, max_length=10)), label="Date of Birth(YYYY-MM-DD)")
    #gender of user
    gender = forms.ChoiceField(widget = forms.RadioSelect, choices = (('1','Male'),('2','Female')), label = 'Gender')
    #profile picture of user
    #profilePic = forms.ImageField() 

class ngoRegistration(forms.Form):
    #name of ngo
    ngoName = forms.RegexField(regex = r'^\w+$', widget = forms.TextInput(attrs = dict(required=True, max_length = 32)), label = "Name of NGO")
    #first name of ngo's manager
    manFirstName = forms.RegexField(regex = r'^\w+$', widget = forms.TextInput(attrs = dict(required=True, max_length = 32)), label = "Manager's First Name")
    #last name of user
    manLastName = forms.RegexField(regex = r'^\w+$', widget = forms.TextInput(attrs = dict(required=True, max_length = 32)), label = "Manager's Last Name")
    #contact number of ngo's manager
    manContactNumber = forms.IntegerField(widget=forms.TextInput(attrs = dict(required=True, max_length = 10)), label = "Manager's Conact Number")
    #address of NGO
    ngoAddress = forms.CharField(widget = forms.TextInput(attrs = dict(required=True, max_length = 100)), label = "Address of the Head Office")
    #Ngo's head office Contact number
    ngoContactNumber = forms.IntegerField(widget=forms.TextInput(attrs = dict(required=True, max_length = 10)), label = "Manager's Conact Number")
    #ngo's description
    ngoDetails = forms.CharField(widget = forms.TextInput(attrs = dict(required=True, max_length=100)), label = "Description of Your NGO")
    #url of the ngo
    ngoURL = forms.URLField(label="NGO's URL:")
    #profile picture of NGO
    #profilePic = forms.ImageField()

class addEvent(forms.Form):
    #evnetDate is the date of the event
    eventDate = forms.DateField(widget = forms.TextInput(attrs=dict(required=True,max_length=10)), label="Date of the Event(YYYY-MM-DD)")
    #eventName is the name of the event
    eventName = forms.CharField(widget = forms.TextInput(attrs=dict(required=True, max_length=50)), label = "Name of Event")
    #eventDetail is the detail of the event
    eventDetail = forms.CharField(widget = forms.TextInput(attrs=dict(required=True, max_length=1000)), label="Event's Details")
