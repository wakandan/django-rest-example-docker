from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_example.serializers import (
    UserSerializer,
    GroupSerializer,
    TypeSerializer,
    ProductSerializer,
    EmployeeSerializer,
)
from rest_framework import generics
from django.db.models import Q


# custom models
from .models import Employee, LocationsEnum, PositionsEnum, Type, Product, StatusEnum


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SearchView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def post(self, request):
        status = request.data.get("status")
        contact_info = request.data.get("contact_info")
        location = request.data.get("location")
        company = request.data.get("company")
        department = request.data.get("department")
        position = request.data.get("position")

        query = Q()
        if status and status in [e.name for e in StatusEnum]:
            query &= Q(status=status)
        if contact_info:
            query &= Q(contact_info=contact_info)
        if location and location in [e.name for e in LocationsEnum]:
            query &= Q(location=location)
        if company:
            query &= Q(company=company)
        if department:
            query &= Q(department=department)
        if position and position in [e.name for e in PositionsEnum]:
            query &= Q(position=position)

        employees = Employee.objects.filter(query)
        return employees
