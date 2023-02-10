import pandas as pd
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class SpecificationViewSet(ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer

    @action(detail=True, methods=["post"], serializer_class=SpecificationCloneSerializer)
    def clone(self, request, *args, **kwargs):
        specification = self.get_object()
        serializer = self.get_serializer(data=request.data, specification=specification)

