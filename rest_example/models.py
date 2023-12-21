from enum import Enum
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField("Is Active", default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField("Product Name", max_length=200)
    price = models.IntegerField("Price", default=0)
    quantity = models.IntegerField("Quantity", default=0)
    description = models.TextField("Description")

    def __str__(self):
        return self.name


class LocationsEnum(Enum):
    HO_CHI_MINH = "Ho Chi Minh"
    SINGAPORE = "Singapore"
    NO_LOCATION = "No Location"


class PositionsEnum(Enum):
    ASSISTANT_MANAGER = "ASSISTANT_MANAGER"
    DIRECTOR = "DIRECTOR"
    OTHER = "OTHER"
    INTERN = "INTERN"
    EMPLOYEE = "EMPLOYEE"
    VICE_PRESIDENT = "VICE_PRESIDENT"


class StatusEnum(Enum):
    ACTIVE = "ACTIVE"
    NOT_STARTED = "NOT_STARTED"
    TERMINATED = "TERMINATED"


class Employee(models.Model):
    first_name = models.CharField("First Name", max_length=200)
    last_name = models.CharField("Last Name", max_length=200)
    contact_info = models.CharField("Contact Info", max_length=200)
    department = models.CharField("Department", max_length=200)
    company = models.CharField("Company", max_length=200, null=True)
    position = models.CharField(
        "Position", max_length=200, choices=[(e.name, e.value) for e in PositionsEnum]
    )
    location = models.CharField(
        "Location", max_length=200, choices=[(e.name, e.value) for e in LocationsEnum]
    )
    status = models.CharField(
        "Status", max_length=200, choices=[(e.name, e.value) for e in StatusEnum]
    )
