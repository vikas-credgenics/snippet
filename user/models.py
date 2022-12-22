from django.db import models
from django.contrib.auth.models import User

from random import randint


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def document_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = 'user_id_' + str(instance.owner.id) + '_' + str(random_with_N_digits(4)) + '.' + ext
    return '/'.join(['user/document', str(instance.owner.id), filename])


class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to=document_path, blank=True, null=True)
    document_type = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s" % self.document
