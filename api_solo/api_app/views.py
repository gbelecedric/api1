from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *

# Create your views here.
def lists (request):
    MAX_OBJECTS = 15
    categorie =Categories.objects.all()[:MAX_OBJECTS]
    data = {"results": list(categorie.values("nom", "description", "image","date_add","date_upd","status",))}
    return JsonResponse(data)

def article (request):
    MAX_OBJECTS = 30
    categorie =Article.objects.all()[:MAX_OBJECTS]
        
        
    data = {"results": list(categorie.values("nom", 
                                             "description",
                                              "image",
                                              "date_add",
                                              "date_upd",
                                              "status",
                                              "souscategorie__nom",
                    
                                                 
                                              
                                              
                                              ))}
    return JsonResponse(data)
    

def detail(request, pk):
    details = get_object_or_404(Categories, pk=pk)
    image = details.image
    data = {"details id={}".format(pk): {
        "nom": details.nom,
        "description": details.description,
        "image": str(image),
        "date_add": details.date_add,
        "date_upd": details.date_upd,
        "status": details.status,
        
    }}
    return JsonResponse(data)
def commentaire (request):
    MAX_OBJECTS = 15
    comment =Commentaire.objects.all()[:MAX_OBJECTS]
    data = {"comment": list(comment.values("user__username", "description", "article__nom","date_add","date_upd","status",))}
    return JsonResponse(data)

def souscategorie (request):
    MAX_OBJECTS = 15
    comment = Souscategorie.objects.all()[:MAX_OBJECTS]
    data = {"comment": list(comment.values("categorie__nom", "description", "article__nom","date_add","date_upd","status",))}
    return JsonResponse(data)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    