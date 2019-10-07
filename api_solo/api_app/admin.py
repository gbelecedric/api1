from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoriesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',

        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = ('status', 'date_add', 'date_upd')


class SouscategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'nom',

        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = ('status', 'date_add', 'date_upd')


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'souscategorie',
        'nom',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = ('status', 'date_add', 'date_upd')


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'article',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = ('status', 'date_add', 'date_upd')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categories, CategoriesAdmin)
_register(models.Souscategorie, SouscategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
