from django.db import models


class agegroup(models.Model):
    state_name = models.CharField(max_length=100)
    is_state = models.IntegerField()
    year = models.IntegerField()
    category = models.CharField(max_length=100)
    type1 = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age_16_18 = models.IntegerField()
    age_18_30 = models.IntegerField()
    age_30_50 = models.IntegerField()
    age_50_above = models.IntegerField()

class periodofsentence(models.Model):
    state_name = models.CharField(max_length=100)
    is_state = models.IntegerField()
    year = models.IntegerField()
    gender = models.CharField(max_length=100)
    sentence_period = models.CharField(max_length=100)
    age_16_18_years = models.IntegerField()
    age_18_30_years = models.IntegerField()
    age_30_50_years = models.IntegerField()
    age_50_above = models.IntegerField()

class education(models.Model):

    state_name = models.CharField(max_length=100)
    is_state = models.IntegerField()
    year = models.IntegerField()
    gender = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    count = models.IntegerField()

class escapes(models.Model):
    state_name = models.CharField(max_length=100)
    year = models.IntegerField()
    detail = models.CharField(max_length=100)
    total = models.IntegerField()
