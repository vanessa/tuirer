from django.urls import reverse_lazy
from django.views import generic

from tuites.forms import PostTuiteForm
from tuites.models import Tuite


class PostTuiteView(generic.CreateView):
    template_name = 'post.html'
    model = Tuite
    form_class = PostTuiteForm
    success_url = reverse_lazy('tuites:post')

    def get_initial(self):
        return {'creator': self.request.user.id}


class ListTuiteView(generic.ListView):
    template_name = 'list.html'
    model = Tuite
    context_object_name = 'tuites'
