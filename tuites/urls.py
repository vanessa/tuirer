from django.urls import path

from tuites.views import ListTuiteView, PostTuiteView, SearchTuiteView, SingleTuiteView, LikeTuiteView

app_name = 'tuites'

urlpatterns = [
    path('postar', PostTuiteView.as_view(), name='post'),
    path('tuites', ListTuiteView.as_view(), name='list'),
    path('buscar', SearchTuiteView.as_view(), name='search'),
    path('tuite/<int:pk>', SingleTuiteView.as_view(), name='tuite'),

    # Actions
    path('tuite/<int:pk>/like', LikeTuiteView.as_view(), name='like'),
]
