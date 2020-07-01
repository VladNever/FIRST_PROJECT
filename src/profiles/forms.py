from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

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


