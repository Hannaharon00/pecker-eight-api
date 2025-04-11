from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..factories import SpecificationFactory


class BuiltSpecificationsReportTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/stuffs/specifications/export_built_specification_report/"

        # Create specifications with different statuses
        self.spec1 = SpecificationFactory(code_number="SPEC001", status="Built")
        self.spec2 = SpecificationFactory(code_number="SPEC001", status="Built")
        self.spec3 = SpecificationFactory(code_number="SPEC002", status="Built")
        self.spec4 = SpecificationFactory(code_number="SPEC003", status="Planning Phase")

