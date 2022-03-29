from django.urls import path
from .views import Dechiffrer , Chiffrer

#chemin correspondant au differnt liens de l'application
urlpatterns = [
    
    #chemin pour le chiffrement 
    
    path('Chiffrer/',Chiffrer,name="Chiffrer"),
    
    #Chemin pour le dechiffrement
    
    path('Dechiffrer', Dechiffrer,name="Dechiffrer"),
]
