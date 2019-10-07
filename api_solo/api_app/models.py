from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='image_categorie')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        

        verbose_name = 'Categories'
        verbose_name_plural = 'Categoriess'

    def __str__(self):
       
        return self.nom


class Souscategorie(models.Model):
   
    categorie = models.ForeignKey(Categories, related_name='categorie_de_souscategorie', on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='image_souscategorie')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
       

        verbose_name = 'Souscategorie'
        verbose_name_plural = 'Souscategories'

    def __str__(self):
        
        return self.nom


class Article(models.Model):
    
    souscategorie = models.ForeignKey(Souscategorie, related_name='souscategorie_of_article', on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='image_souscategorie')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
      
        return self.nom



class Commentaire(models.Model):
   
    user = models.ForeignKey(User,related_name='User_commentaire',on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='commentaire_of_article', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
       

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'
