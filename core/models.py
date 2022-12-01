from django.db import models


class Token(models.Model):
    name = models.CharField(max_length=16, unique=True, db_index=True)
    social_volumes = models.FloatField(null=True)
    social_contributes = models.FloatField(null=True)