import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

from stats.models import Vote
print(Vote.objects.all())