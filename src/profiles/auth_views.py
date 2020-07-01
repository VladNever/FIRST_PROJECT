from django.contrib.auth.views import LoginView, LogoutView


class MyLogin(LoginView):
    template_name = 'auth/login.html'
class MyLogout(LogoutView):
    pass



