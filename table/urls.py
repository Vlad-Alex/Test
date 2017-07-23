from django.conf.urls import url
from . import views

urlpatterns = [
       #Main Worklist /table/
       url(r'^$', views.index, name='index'),
       #Worklist/Countries/
    url(r'^(?P<worklist_id>[0-9]+)/$',views.detail, name='detail'),

]