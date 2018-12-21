from django.conf.urls import url
from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

