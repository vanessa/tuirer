from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import HttpResponseRedirect

from users.forms import SignupForm
from users.models import User


class LoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass


class SignupView(generic.CreateView):
    form_class = SignupForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('tuites:list')

    def form_valid(self, form):
        user = form.save()
        new_user = authenticate(
            username=user.username,
            password=self.request.POST.get('password1'),
        )
        login(self.request, new_user)
        messages.info(
            self.request,
            'Obrigado por se cadastrar, {0}!'.format(user.username)
        )
        return HttpResponseRedirect(self.success_url)


class ProfileView(generic.DetailView):
    template_name = 'profile.html'
    model = User
    context_object_name = 'user'
