from random import sample

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from stuffs.factories import ComponentFactory, GroupFactory, SpecificationFactory


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        specifications = SpecificationFactory.create_batch(10)
        current_specification = specifications[-1]

