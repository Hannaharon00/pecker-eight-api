from django.test import TestCase
from rest_framework.exceptions import ValidationError

from stuffs.factories import ComponentFactory, GroupFactory, SpecificationFactory
from stuffs.serializers import (
    ComponentSerializer,
    GroupSerializer,
    PartCodeAssignmentSerializer,
    SpecificationCloneSerializer,
    SpecificationSerializer,
)


class SpecificationSerializerTest(TestCase):
    def setUp(self):
        self.specification = SpecificationFactory()
        self.group = GroupFactory(specification=self.specification)
        self.component = ComponentFactory(specification=self.specification, group=self.group)

    def test_validate_completed(self):
        self.specification.completed = True
        serializer = SpecificationSerializer(self.specification, data={"completed": True}, partial=True)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

        self.component.part_code = "PART001"
        self.component.save()
        serializer = SpecificationSerializer(self.specification, data={"completed": True}, partial=True)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["completed"], True)

