from django.conf.urls import url
from . import views

urlpatterns = [
 
    url(r'^$',views.home,name='home'),
    url(r'^triplist/$',views.triplist,name='triplist'),
    url(r'^trip/$',views.trip_content,name='trip'),
    url(r'^user/',views.user_data,name='user'),
    url(r'^trip/(?P<id>\d+)$', views.tripdetail, name="trip"),


]

