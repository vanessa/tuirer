from django.views import generic

from tuites.models import Tuite


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tuites'] = Tuite.objects.all()[:2]
        return context
