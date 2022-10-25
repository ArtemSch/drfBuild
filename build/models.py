from django.db import models
from model_utils.models import TimeStampedModel


class ResidentialComplex(TimeStampedModel):
    year_construction = models.IntegerField(blank=True, null=True)
    quarter = models.CharField(unique=True, max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    developer = models.CharField(max_length=255, blank=True, null=True)
