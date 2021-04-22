from django.urls import path, include
from stockColi import views 

urlpatterns = [

    path('api/depots', views.depot_list, name='depot_list'),
    path('api/envois', views.envoi_list, name='envoi_list'),
    
   

]
