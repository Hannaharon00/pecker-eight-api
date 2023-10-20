from copy import deepcopy

from django.db.models import Q
from rest_framework import serializers

from .models import Component, Group, Specification


class SpecificationSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.StringRelatedField(many=True, read_only=True)
    components = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Specification
        fields = "__all__"

    def validate_completed(self, value):
        if value and self.instance.components.filter(Q(part_code=None) | Q(part_code="")).exists():
            raise serializers.ValidationError("Cannot complete a specification if any component is missing a part.")

        return value

        return data


    class Meta:
        model = Group
        fields = "__all__"
        read_only_fields = ("specification",)


    def __init__(self, *args, **kwargs):
        specification = kwargs.pop("specification", None)
        super().__init__(*args, **kwargs)

    @property
    def instance_specification(self):
        if hasattr(self, "instance") and isinstance(self.instance, Component):
            return self.instance.specification
        return None

    def validate(self, data):
        if self.specification and self.specification.completed:
            raise serializers.ValidationError("Cannot create/update a component of a completed specification.")

