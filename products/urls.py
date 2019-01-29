from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.products, name='products'),
	# url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    ]