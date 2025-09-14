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
                            "components": [
                                {"name": "Component 1", "description": "This is component 1", "part_code": "PART001"},
                                {"name": "Component 2", "description": "This is component 2", "part_code": "PART002"},
                            ],
                        },
                        {
                        },
                    ],
                }
            ]
        }


    def test_import_specifications_invalid_data(self):
        invalid_payload = {
            "specifications": [
                {"name": "", "code_number": "SPEC001", "completed": False, "status": "Planning Phase", "groups": []}
            ]
