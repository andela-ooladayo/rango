from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return '%s' % self.title
