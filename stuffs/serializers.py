from copy import deepcopy

from .models import Component, Group, Specification


class SpecificationSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.StringRelatedField(many=True, read_only=True)
    components = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Specification
        fields = "__all__"

        return data


    class Meta:
        model = Group
        fields = "__all__"
        read_only_fields = ("specification",)

