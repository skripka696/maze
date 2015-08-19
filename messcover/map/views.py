from django.views.generic import TemplateView, ListView
from django.shortcuts import render, render_to_response, redirect
from models import My_Tree
# import tasks
import actions


class Start(TemplateView):
    template_name = 'map/start.html'


class Parse(TemplateView):
    template_name = 'map/parse.html'

    def get_context_data(self, **kwargs):
        context = super(Parse, self).get_context_data(**kwargs)
        actions.run_spider()
        # tasks.run_spider()
        return context


class Tree(ListView):
    model = My_Tree
    template_name = 'map/tree.html'

    def get(self, request, *args, **kwargs):
        tree = My_Tree.objects.all()
        print tree
        return render(request, self.template_name, {'nodes': tree})

