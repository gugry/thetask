# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class MessageModel(models.Model):
    message_status = models.BooleanField()
    message_text = models.TextField()
    def __str__(self):
        return self.message_text

