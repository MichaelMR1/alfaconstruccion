from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Dashboard(TemplateView):
    # template_name = 'dashboard2.html'
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['breadcrumbs'] = [
        #     {'name': 'Indicadores', 'url': None}
        #     ]
        return context