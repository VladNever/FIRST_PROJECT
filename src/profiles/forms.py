from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
from django.contrib.auth.models import Group
from django import forms

class CreateProfileForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 
                                                'phone_number', 'country', 'city', 'index', 
                                                'adress1', 'adress2', 'additionally')

class UpdateProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Profile
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 
                                                'phone_number', 'country', 'city', 'index', 
                                                'adress1', 'adress2', 'additionally')

class UpdateProfileFormManager(forms.ModelForm):
    #groups = forms.ModelMultipleChoiceField( 
    #    queryset=Group.objects.all(),
    #    to_field_name='name',
    #    widget=forms.CheckboxSelectMultiple,
    #)
    class Meta(UserChangeForm.Meta):
        model = Profile
        fields = ('first_name', 'last_name', 'email', 
                    'phone_number', 'country', 'city', 'index', 
                    'adress1', 'adress2', 'additionally', 'is_staff', 
                    #'groups'
                )



