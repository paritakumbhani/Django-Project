"""djangoAssignment3 URL Configuration """

from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    re_path(r'',include('application.urls')),
    path('admin/', admin.site.urls),
]
