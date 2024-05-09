# stuffs/factories.py

import factory
from factory.django import DjangoModelFactory

from .models import Component, Group, Specification


class SpecificationFactory(DjangoModelFactory):
    class Meta:
        model = Specification

    name = factory.Faker("word")
    code_number = factory.Faker("ean8")
    completed = False
    status = "Planning Phase"


