from django.contrib.auth import views as auth_views
from django.views import generic

from users.models import User


class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass


class ProfileView(generic.DetailView):
    template_name = 'profile.html'
    model = User
    context_object_name = 'user'
