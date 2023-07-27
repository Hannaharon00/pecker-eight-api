import pandas as pd
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.viewmixins import NestedObjectMixin
from core.viewsets import CreateListViewSet, RetrieveUpdateDestroyViewset

from .models import Component, Group, Specification
from .serializers import (
    ComponentSerializer,
    GroupSerializer,
    PartCodeAssignmentSerializer,
    SpecificationCloneSerializer,
    SpecificationImportSerializer,
    SpecificationSerializer,
)


class SpecificationViewSet(ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer

    @action(detail=True, methods=["post"], serializer_class=SpecificationCloneSerializer)
    def clone(self, request, *args, **kwargs):
        specification = self.get_object()
        serializer = self.get_serializer(data=request.data, specification=specification)

    @action(detail=False, methods=["post"], serializer_class=SpecificationImportSerializer)
    def import_data(self, request):
        serializer = SpecificationImportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "Specifications imported successfully!"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
