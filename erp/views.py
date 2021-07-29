from django.template import loader

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Informes, Clientes, Pagos

# Create your views here.


#def index(request):
    #return HttpResponse("BIEN VENIDO A INNOVA-IT.")


class IndexView(generic.ListView):
    template_name = 'erp/index.html'
    context_object_name = 'latest_clientes_list'

    def get_queryset(self):
        """Return the last five published clientes."""
        return Clientes.objects.order_by('-pub_date')[:5]

#def detail(request, clientes_id):
 #   return HttpResponse("You're looking at question %s." % clientes_id)
class DetailView(generic.DetailView):
    model = Clientes
    template_name = 'erp/detail.html'


#def results(request, clientes_id):
 #   clientes = get_object_or_404(Clientes, pk=clientes_id)
  #  return render(request, 'monitoreo/results.html', {'clientes': clientes})
class ResultsView(generic.DetailView):
    model = Clientes
    template_name = 'erp/results.html'

def vote(request, clientes_id):
    clientes = get_object_or_404(Clientes, pk=clientes_id)
    try:
        selected_informes = clientes.informes_set.get(pk=request.POST['informes'])
    except (KeyError, informes.DoesNotExist):
        # Redisplay the clientes voting form.
        return render(request, 'erp/detail.html', {
            'clientes': clientes,
            'error_message': "You didn't select a informes.",
        })
    else:
        selected_informes.votes += 1
        selected_informes.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('erp:results', args=(clientes.id,)))