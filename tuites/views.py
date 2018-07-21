from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

from tuites.forms import PostTuiteForm
from tuites.models import Tuite


class PostTuiteView(generic.CreateView):
    template_name = 'post.html'
    model = Tuite
    form_class = PostTuiteForm
    success_url = reverse_lazy('tuites:list')

    def get_initial(self):
        return {'creator': self.request.user.id}

    def form_valid(self, form):
        messages.success(self.request, 'Você enviou um Tuite! Veja ele abaixo.')
        return super().form_valid(form)


class ListTuiteView(generic.ListView):
    template_name = 'list.html'
    model = Tuite
    context_object_name = 'tuites'
