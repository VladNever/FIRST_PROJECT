from django.urls import reverse_lazy
from .models import Profile
from .forms import CreateProfileForm, UpdateProfileForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import DetailView


class CreateProfile(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'profiles/create_profile.html'
    def get_success_url(self):
        return reverse_lazy('homepage:homepage') 

class UpdateProfile(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'profiles/update_profile.html'
    def get_success_url(self):
        return reverse_lazy('homepage:homepage')

class DetailProfile(DetailView):
    model = Profile
    template_name = 'profiles/detail_profile.html'

#class ListGenre(ListView):
#    model = Genre
#    template_name = 'ref_books/list_genre.html'

#class DeleteGenre(PermissionRequiredMixin, DeleteView):
#    permission_required = 'ref_books.delete_genre'
#    model = Genre
#    template_name = 'ref_books/delete_genre.html'
#    def get_success_url(self):
#        return reverse_lazy('ref_books:list_genre')



