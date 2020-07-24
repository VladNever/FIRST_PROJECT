from django.urls import path
from profiles.views import CreateProfile, UpdateProfile, DetailProfile
from profiles.views import ListProfilesManager, UpdateProfileManager

app_name = "profile"


urlpatterns = [
    path('create-profile/', CreateProfile.as_view(), name="create"),
    path('update-profile/<int:pk>', UpdateProfile.as_view(), name="update"),
    path('detail-profile/<int:pk>', DetailProfile.as_view(), name="detail"),
    path('list-profiles-manager/', ListProfilesManager.as_view(), name="list_manager"),
    path('update-profile-manager/<int:pk>', UpdateProfileManager.as_view(), name="update_manager"),
]