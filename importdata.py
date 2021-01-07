import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()

from mainsite.models import Branch

data_title = list()
data_name = list()
with open