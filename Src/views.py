from django.shortcuts import render
#fonction permettant d'afficher la page index
def Index(request):
    return render(request,"index.html")
