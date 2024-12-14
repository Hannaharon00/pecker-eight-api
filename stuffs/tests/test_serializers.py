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

    def test_validate_completed_with_parts(self):
        self.component.part_code = "PART001"
        self.component.save()
        serializer = SpecificationSerializer(self.specification, data={"completed": True}, partial=True)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["completed"], True)

    def test_validate_modification_of_completed_specification(self):
        self.specification.completed = True
        self.specification.save()
        serializer = SpecificationSerializer(self.specification, data={"name": "New Name"}, partial=True)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

class GroupSerializerTest(TestCase):
    def setUp(self):
        self.specification = SpecificationFactory()
        self.group = GroupFactory(specification=self.specification)

        GroupFactory(name="Test Group", specification=another_specification)
        serializer = GroupSerializer(
            data={"name": "Test Group", "group_code": "GRP004"}, specification=self.specification
        )
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

        self.specification.save()
        serializer = GroupSerializer(
            data={"name": "New Group", "group_code": "GRP003"}, specification=self.specification
        )
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

