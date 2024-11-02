from django.db import models
from .utils import libs
import time

class User(models.Model):
    uuid = models.CharField(max_length=100,db_index=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    introduction = models.CharField(max_length=500)
    membership = models.IntegerField()
    membership_date = models.CharField(max_length=30,null=True, blank=True)
    create_at = models.IntegerField()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'project_user'
        ordering = ['-id']
        verbose_name = 'user'
        verbose_name_plural = "会员"

    def to_dict(self):
        return {'id': self.id,'email':self.email,'membership':self.membership,'introduction':self.introduction,'membership_date':self.membership_date, 'create_at':libs.timeTransfer(self.create_at)}
    