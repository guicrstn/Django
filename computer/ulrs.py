from django.urls import path

from computer.views import ClientDetailView, ClientsListView, ComputersListView, InterfacesListView, BuildDevView, IndexPageView

app_name = 'computer'
urlpatterns = [

    # Page d'accueil
    path('',
    IndexPageView.as_view(),
    name='index'),

    # Page Interfaces
    path('interfaces/',
    InterfacesListView.as_view(),
    name='interfaces'),
  
    #Page Computer
    path('ordinateurs/',
    ComputersListView.as_view(),
    name='ordinateurs'),
    # TODO : Ajouter les routes.

    path('clients/',
    ClientsListView.as_view(),
    name='clients'),

    path('client/',
    ClientDetailView.as_view(),
    name='client'),

    path('login/',
    BuildDevView.as_view(),
    name='login'),

    path('edit/',
    BuildDevView.as_view(),
    name='edit'),
]