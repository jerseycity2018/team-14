from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from .models import UserSurvey, WasteTracking, VolunteerTracking

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)

class UserSurveyForm(forms.ModelForm):

    class Meta:
        model = UserSurvey
        fields = [
            'isNYCHA',
            'building',
            'referredBy',
        ]

class WasteTrackingForm(forms.ModelForm):

    class Meta:
        model = WasteTracking
        fields = [
         'volunteer',
         'wasteWeight',
        ]

class VolunteerTrackingForm(forms.ModelForm):

    class Meta:
        model = VolunteerTracking
        fields = [
         'volunteer',
         'VolunteerTime',  
        ]