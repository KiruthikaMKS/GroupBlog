from django.conf.urls import url
from . import views as v

app_name = 'posts'

urlpatterns = [
    url(r'^$',v.ListPost.as_view(),name='all'),
    url(r'new/post/$',v.CreatePost.as_view(),name='create'),
    url(r'post/@/(?P<username>[-\w]+)/(?P<pk>\d+)/$',v.SinglePost.as_view(),name='single'),
    url(r'posts/by/(?P<username>[-\w]+)/$',v.UserPost.as_view(),name='for_user'),
    url(r'delete/(?P<pk>\d+)/$',v.DeletePost.as_view(),name='delete'),
]
