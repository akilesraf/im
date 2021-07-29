from django.urls import path


from . import views

app_name = 'erpe'
urlpatterns = [
    
    # ex: /monitoreo/
    path('', views.IndexView.as_view(), name='INNOVA-IT'),
    # ex: /monitoreo/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /monitoreo/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /monitoreo/5/vote/
    path('<int:clientes_id>/vote/', views.vote, name='vote'),
]
