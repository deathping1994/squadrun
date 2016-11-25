from __future__ import unicode_literals

from django.db import models
from ..core.models import BaseModel, User
# Create your models here.


class Ticket(BaseModel):
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=150)
    assigned_to = models.ForeignKey(User)
    STATUS_CHOICES = (
        ('R', 'Resolved'),
        ('P', 'Pending'),
        ('U', 'More info needed'),
        ('C', 'Closed'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


class Reply(BaseModel):
    ticket = models.ForeignKey(Ticket)
    attachment = models.CharField(max_length=2048)
    text = models.CharField(max_length=500)