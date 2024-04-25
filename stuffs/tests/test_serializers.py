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

