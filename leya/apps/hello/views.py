
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView

from .models import Hello

class HelloCreateView(CreateView):
    model = Hello
    template_name = 'hello_create_form.html'
    success_url = reverse_lazy('hello:list')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Hello.objects.all()
        return super(HelloCreateView, self).get_context_data(**kwargs)

class HelloListView(ListView):
    template_name = 'hello_list.html'
    queryset = Hello.objects.all()

class HelloRemoveView(DeleteView):
    model = Hello
    success_url = reverse_lazy('hello:list')