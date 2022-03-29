from importlib.resources import path
from .chiffrement import ChiffrementCesar
from .dechiffrement import DechiffrementCesar
from pyexpat.errors import codes
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render

#fonction pour l'affichage du template de dechiffrement 

def Dechiffrer(request):
    Donnee = ''
    if request.method == 'POST':
        
        #recupération du message á déchiffré
        
        messageDechiffrer = request.POST.get("messageDechiffrer") 
        try:
            #recupération et conversion du clé de Dechiffrement en un nombre entier
            
            Cle = -int(request.POST.get("Cle")) 
            
            Donnee = DechiffrementCesar(messageDechiffrer,Cle)
        except:
            
            #Réaffichage de la page de déchiffrement si l'un des champ est vide 
            
           return HttpResponseRedirect(request.path) 
    return render(request,"Dechiffrement.html",context={"values":Donnee})

#fonction pour l'affichage du template de chiffrement

def Chiffrer(request):
    data = ''
    if request.method == "POST":
        
         #recupération du message á déchiffré
         
        Message = request.POST.get("Message")
        try:
            #recupération et conversion du clé de Dechiffrement en un nombre entier
            
            Cle = int(request.POST.get("Cle"))
            data = ChiffrementCesar(Message,Cle)
        except:
            
            #Réaffichage de la page de déchiffrement si l'un des champ est vide 
            
           return HttpResponseRedirect(request.path)
    return render(request,"Chiffrement.html",context={"Values":data})
# Create your views here.
