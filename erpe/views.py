from django.template import loader

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Informe, Cliente
# Create your views here.


#def index(request):
    #return HttpResponse("BIEN VENIDO A INNOVA-IT.")


class IndexView(generic.ListView):
    template_name = 'erpe/index.html'
    context_object_name = 'latest_cliente_list'

    def get_queryset(self):
        """Return the last five published cliente."""
        return Cliente.objects.order_by('-pub_date')[:5]

#def detail(request, clientes_id):
 #   return HttpResponse("You're looking at question %s." % clientes_id)
class DetailView(generic.DetailView):
    model = Cliente
    template_name = 'erpe/detail.html'


#def results(request, clientes_id):
 #   clientes = get_object_or_404(Clientes, pk=clientes_id)
  #  return render(request, 'monitoreo/results.html', {'clientes': clientes})
class ResultsView(generic.DetailView):
    model = Cliente
    template_name = 'erpe/results.html'

def vote(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    try:
        selected_informe = cliente.informe_set.get(pk=request.POST['informe'])
    except (KeyError, informe.DoesNotExist):
        # Redisplay the clientes voting form.
        return render(request, 'erpe/detail.html', {
            'cliente': cliente,
            'error_message': "You didn't select a informe.",
        })
    else:
        selected_informe.votes += 1
        selected_informe.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('erpe:results', args=(cliente.id,)))
