from django.conf.urls import url
from . import views as v

app_name = 'groups'

urlpatterns = [
    url(r'^$',v.ListGroup.as_view(),name='all'),
    url(r'single/(?P<slug>[-\w]+)/$',v.SingleGroup.as_view(),name='single'),
    url(r'join/(?P<slug>[-\w]+)/$',v.JoinGroup.as_view(),name='join'),
    url(r'leave/(?P<slug>[-\w]+)/$',v.LeaveGroup.as_view(),name='leave'),
    url(r'create/$',v.CreateGroup.as_view(),name='create'),
]
