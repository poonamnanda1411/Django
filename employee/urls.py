from django.urls import path

from . import views
from .views import *

urlpatterns=[
    path('',home,name='Employee'),
    path('add',add,name='add'),
    path('',create_view, name='Employee'),
    path('',list_view, name='Employee'),
    path('<id>/delete', delete_view,name='Employee'), 
    path('<id>/update', update_view,name='Employee'), 
    path('<id>',detail_view, name='Employee'),
    ]