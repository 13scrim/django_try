import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccesRecord,webpage,Topic

from faker import Faker

topics = ['Social','Marketing','Grosserie','Search','Games','News']

fakegen = Faker()
def add_topic():
    t = Topic.objects.get_or_create(top_name= random.choice(topics))[0] #get_or_create return a tuple and we need the first entry
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fkurl = fakegen.url()
        fkdate = fakegen.date()
        fkname = fakegen.name()

        web = webpage.objects.get_or_create(topic = top,name = fkname, url=fkurl )[0]
        acces = AccesRecord.objects.get_or_create(name = web,date = fkdate)[0]



if __name__ == '__main__':
    print("population script!")
    populate(20)
    print("Populate complete")
