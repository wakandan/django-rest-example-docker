"""django_rest_example_docker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]
"""

from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_example import views as rest_example_views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", rest_example_views.UserViewSet)
router.register(r"groups", rest_example_views.GroupViewSet)
# register custom models
router.register(r"types", rest_example_views.TypeViewSet)
router.register(r"products", rest_example_views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/", rest_example_views.SearchView.as_view()),
    path(r"^", include(router.urls)),
    path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
