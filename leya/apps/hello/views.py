
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Hello

class HelloCreateView(CreateView):
    model = Hello
    template_name = 'hello_create_form.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Hello.objects.all()
        return super(HelloCreateView, self).get_context_data(**kwargs)

class HelloListView(ListView):
    model = Hello
    context_object_name = 'object_list'
    template_name = 'hello_list.html'