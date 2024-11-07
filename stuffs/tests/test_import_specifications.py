from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Component, Group, Specification


            "specifications": [
                {
                    "name": "Specification 1",
                    "code_number": "SPEC001",
                    "completed": False,
                    "status": "Planning Phase",
                    "groups": [
                        {
                            "name": "Group 1",
                            "group_code": "GRP001",
