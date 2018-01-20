from django.conf.urls import url
from accounts.views import SignUp
from django.contrib.auth import views as v

app_name = 'accounts'

urlpatterns =[
    url(r'^signup/$',SignUp.as_view(),name='signup'),
    url(r'^login/$',v.LoginView.as_view(),name='login'),
    url(r'^logout/$',v.LogoutView.as_view(),name='logout'),
]
