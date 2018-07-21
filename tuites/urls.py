from django.urls import path

from tuites.views import ListTuiteView, PostTuiteView

app_name = 'tuites'

urlpatterns = [
    path('postar', PostTuiteView.as_view(), name='post'),
    path('tuites', ListTuiteView.as_view(), name='list'),
]
