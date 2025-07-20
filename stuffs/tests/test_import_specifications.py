from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Component, Group, Specification


class ImportSpecificationsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/stuffs/specifications/import_data/"
        self.valid_payload = {
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
                        },
                    ],
                }
            ]
        }

