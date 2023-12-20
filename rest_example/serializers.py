from django.contrib.auth.models import User, Group
from rest_framework import serializers

# custom models
from .models import Employee, Type, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "first_name",
            "last_name",
            "contact_info",
            "department",
            "position",
            "location",
            "status",
        )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("url", "name")


# create serializer for custom models
class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ("name", "active")


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ("type_id", "name", "price", "quantity", "description")
