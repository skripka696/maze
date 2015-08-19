from django.contrib import admin
from .models import My_Tree
from django_mptt_admin.admin import DjangoMpttAdmin


class TreeAdmin(DjangoMpttAdmin):
    list_display = ('url',)


admin.site.register(My_Tree, TreeAdmin)
