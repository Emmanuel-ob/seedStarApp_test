from django.conf.urls import url
from . import views


app_name = 'myApp'

urlpatterns = [

        url(r'^$', views.renderHome, name='index'), 
        url(r'^list$', views.getList, name='list'), 
        url(r'^add$', views.getAdd, name='add'), 
         
 ]      