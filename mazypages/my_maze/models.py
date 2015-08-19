from django.db import models

class Route(models.Model):
    start_url = models.URLField()
    end_url = models.URLField()

    def __unicode__(self):
        return '{0} {1}'.format(self.start_url, self.end_url)