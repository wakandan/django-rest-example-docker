from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_example.serializers import (
    UserSerializer,
    GroupSerializer,
    EmployeeSerializer,
)
from rest_framework import generics
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView


# custom models
from .models import Employee, LocationsEnum, PositionsEnum, StatusEnum


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


class SearchView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request):
        data = request.query_params
        status = data.get("status")
        contact_info = data.get("contact_info")
        location = data.get("location")
        company = data.get("company")
        department = data.get("department")
        position = data.get("position")

        query = Q()
        if status:
            query &= Q(status=status)
        if contact_info:
            query &= Q(contact_info=contact_info)
        if location:
            query &= Q(location=location)
        if company:
            query &= Q(company=company)
        if department:
            query &= Q(department=department)
        if position:
            query &= Q(position=position)

        employees = Employee.objects.filter(query)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
