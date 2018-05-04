import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_project1.settings')

import django
django.setup()

## Fake Data Script
import random
from first_app.models import AccessRecodrd, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics =['Search','Social', 'Marketplace','News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):

    for entry in range(N):
        # Topic
        top = add_topic()

        #Generate Fake Data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #Generate Fake Webpage
        webpg =  Webpage.objects.get_or_create(topic=top, url=fake_url, name = fake_name)[0]

        #Generate Access Record
        acc_rec = AccessRecodrd.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Fake Data")
    populate(20)
    print("End the populating! Good Bye")
