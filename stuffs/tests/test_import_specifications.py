from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Component, Group, Specification


                    "status": "Planning Phase",
                    "groups": [
                        {
                            "name": "Group 1",
                            "group_code": "GRP001",
