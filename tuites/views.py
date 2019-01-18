from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from tuites.forms import PostTuiteForm
from tuites.models import Tuite


class PostTuiteView(LoginRequiredMixin, generic.CreateView):
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


class LikeTuiteView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        tuite_pk = kwargs.get('pk')
        tuite = Tuite.objects.get(pk=tuite_pk)

        # Pega URL de onde o usuário fez a requisição
        # https://stackoverflow.com/a/38525699/4526204
        url = self.request.META.get('HTTP_REFERER')

        # Passos para implementação da curtida:
        # 1. Checar se o usuário está logado, isso pode ser,
        #    feito usando LoginRequiredMixin ☑️
        # 2. Checar se o usuário já curtiu ou não este Tuite,
        #    e descurtir caso verdadeiro ☑️
        # 3. Computar a curtida/descurtida no Tuite ☑️

        user_already_liked = self.request.user.liked_tuites.filter(
            pk__in=[tuite_pk]).exists()

        if user_already_liked:
            # Remove o like do Tuite para o usuário
            self.request.user.liked_tuites.remove(tuite)

            # Mostra uma mensagem de feedback para o usuário
            messages.success(
                self.request,
                'Você descurtiu o Tuite!'
            )
            return url

        # Adiciona o Tuite aos likes do usuário
        # se ele já não tiver curtido
        self.request.user.liked_tuites.add(tuite)

        # Mostra uma mensagem de feedback para o usuário
        messages.success(self.request, 'Você curtiu este Tuite!')

        return url
