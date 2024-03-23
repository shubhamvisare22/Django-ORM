import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OrmMastery.settings')  
django.setup()

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from OrmMasteryApp.models import Author, Publisher, Book, Genre
from django_seed import Seed

def generate_seed_data():
    seeder = Seed.seeder()

    # Add authors
    seeder.add_entity(Author, 5, {
        'name': lambda x: seeder.faker.name(),
        'email': lambda x: seeder.faker.email()
    })

    # Add publishers
    seeder.add_entity(Publisher, 3, {
        'name': lambda x: seeder.faker.company(),
        'website': lambda x: seeder.faker.url()
    })

    # Add genres
    seeder.add_entity(Genre, 5, {
        'name': lambda x: seeder.faker.word()
    })

    # Add books
    seeder.add_entity(Book, 10, {
        'title': lambda x: seeder.faker.sentence(),
        'publisher': lambda x: seeder.faker.random_element(Publisher.objects.all()),
        'publication_date': lambda x: seeder.faker.date_this_decade(),
        'genre': lambda x: seeder.faker.random_element(Genre.objects.all())
    })

    # Execute seeding
    seeder.execute()


if __name__ == '__main__':
    generate_seed_data()
