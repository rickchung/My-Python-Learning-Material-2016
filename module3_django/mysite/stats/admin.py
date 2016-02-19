from django.contrib import admin

from .models import Candidate, Vote, Region

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Vote)
admin.site.register(Region)