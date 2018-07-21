from django.urls import path

from users.views import LoginView, LogoutView, ProfileView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/<int:pk>', ProfileView.as_view(), name='profile'),
]
