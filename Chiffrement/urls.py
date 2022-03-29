from django.urls import path
from .views import Dechiffrer , Chiffrer


urlpatterns = [
    path('Chiffrer/',Chiffrer,name="Chiffrer"),
    path('Dechiffrer', Dechiffrer,name="Dechiffrer"),
]
