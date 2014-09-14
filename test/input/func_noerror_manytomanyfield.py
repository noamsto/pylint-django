"""
Checks that Pylint does not complain about various
methods on many-to-many relationships
"""
#  pylint: disable=C0111
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    good = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    wrote = models.ManyToManyField(Book)

    def get_good_books(self):
        return self.wrote.filter(good=True)

    def is_author_of(self, book):
        return book in list(self.wrote.all())

    def wrote_how_many(self):
        return self.wrote.count()

    def __unicode__(self):
        return self.name