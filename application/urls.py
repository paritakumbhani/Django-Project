from django.urls import re_path ,include
from . import views

urlpatterns = [
    re_path(r'^addnew', views.addNew),    
    re_path(r'^$', views.show),
    re_path(r'^show', views.show),
    re_path(r'^editpage', views.editpage),
    re_path(r'^update', views.update),
    re_path(r'^delete', views.delete),
    re_path(r'^reset', views.reset),    
    re_path(r'^filter', views.userFilter),    


]
