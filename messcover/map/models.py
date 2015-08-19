from django.db import models
import mptt
from mptt.models import MPTTModel, TreeForeignKey


class My_Tree(models.Model):
    url = models.URLField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    link = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)

    # def __unicode__(self):
    #     return '{0} {1}'.format(self.url, self.name)

mptt.register(My_Tree, )
