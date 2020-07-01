from django.urls import path
from profiles.views import CreateProfile, UpdateProfile, DetailProfile

app_name = "profile"


urlpatterns = [
    path('create-profile/', CreateProfile.as_view(), name="create"),
    path('update-profile/<int:pk>', UpdateProfile.as_view(), name="update"),
    path('detail-profile/<int:pk>', DetailProfile.as_view(), name="detail"),
]