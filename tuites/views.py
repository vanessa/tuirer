from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

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


class SearchTuiteView(generic.ListView):
    template_name = 'search.html'
    model = Tuite
    context_object_name = 'tuites'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Queremos colocar no template o que o usuário buscou,
        # para fins de feedback
        context['query'] = self.request.GET.get('query', None)
        return context

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query is not None:
            return Tuite.objects.search(query)
        return Tuite.objects.none()


class SingleTuiteView(generic.DetailView):
    template_name = 'single_tuite.html'
    model = Tuite
    context_object_name = 'tuite'
