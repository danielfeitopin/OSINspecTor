from django.conf.urls import url
from app import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^dominio/', views.dominio, name='dominio'),
	url(r'^ip/', views.ip, name='ip'),
	url(r'^logout/$', views.logout_view, name= 'logout_view'),
    url(r'^signup/$', views.signup_view, name= 'signup_view'),
]