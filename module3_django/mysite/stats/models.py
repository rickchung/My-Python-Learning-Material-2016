from django.db import models

# Create your models here.
class Candidate(models.Model):
    candidate_name   = models.CharField(max_length=32)
    candidate_gender = models.CharField(max_length=16)
    candidate_age    = models.IntegerField()
    register_date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.candidate_name
    
class Region(models.Model):
    region_name  = models.CharField(max_length=32)

    def __str__(self):
        return self.region_name

class Vote(models.Model):
    candidate  = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    region     = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.candidate) + ', ' + str(self.region)
    