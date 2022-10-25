from django.views.generic import ListView, TemplateView, FormView
from computer.forms import ClientForm
from computer.models import Client, Interface, Computer

BASE_TEMPLATE = 'computer/{page}.html'

class IndexPageView(TemplateView):
    '''
    Page d'accueil du site.
    '''
    template_name = BASE_TEMPLATE.format(page='index')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class InterfacesListView(ListView): # TODO : Ajouter un héritage pour répondre à la demande.
    '''
    Liste des interfaces.
    '''
    template_name = BASE_TEMPLATE.format(page='table')
    model = Interface
    paginate_by = 10

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

     
    # TODO : Afficher les interfaces 10 par 10.

class InterfaceDetailView(): # TODO : Ajouter un héritage pour répondre à la demande.
    '''
    Page du détail d'une interface.
    '''
    pass # TODO : Afficher une interface spécifique.

class ComputersListView(ListView): # TODO : Ajouter un héritage pour répondre à la demande.
    '''
    Liste des ordinateurs.
    '''
    template_name = BASE_TEMPLATE.format(page='ordinateur')
    model = Computer
    paginate_by = 10

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    # TODO : Afficher les ordianteurs 10 par 10.

class ComputerDetailView(): # TODO : Ajouter un héritage pour répondre à la demande.
    '''
    Page du détail d'un ordinateur.
    '''
    pass # TODO : Afficher un ordinateur spécifique.

class ClientsListView(ListView): # TODO : Ajouter un héritage pour répondre à la demande.
    '''
    Liste des clients.
    '''
    template_name = BASE_TEMPLATE.format(page='clients')
    model = Client
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class ClientDetailView(FormView): # TODO : Ajouter un héritage pour répondre à la demande.
    '''
    Page du détail d'un client.
    '''
    template_name = BASE_TEMPLATE.format(page='client')
    form_class = ClientForm

class BuildDevView(TemplateView):

    template_name = BASE_TEMPLATE.format(page='login')
    template_name = BASE_TEMPLATE.format(page='edit')    
