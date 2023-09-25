# liftProj/urls.py

from django.contrib import admin
from django.urls import path, include  # make sure to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uplift.urls')),  # include the URLs of the uplift app
]
