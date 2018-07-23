from django.urls import path

from users.views import LoginView, LogoutView, ProfileView, SignupView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', SignupView.as_view(), name='signup'),
    path('perfil/<int:pk>', ProfileView.as_view(), name='profile'),
]
