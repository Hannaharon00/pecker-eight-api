from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404


class NestedObjectMixin:
    parent_model = None
    parent_object_lookup_field = "pk"

