from django.test import TestCase
from rest_framework.exceptions import ValidationError

    GroupSerializer,
    PartCodeAssignmentSerializer,
    SpecificationCloneSerializer,
    SpecificationSerializer,
)


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

