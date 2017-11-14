from __future__ import unicode_literals

from django.db import models


class Blogs(models.Model):
    url = models.TextField(primary_key=True, unique=True)
    host = models.TextField()
    title = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'blogs'
