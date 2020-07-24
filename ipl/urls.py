from django.conf.urls import url
from django.contrib.auth import views as auth_view

from ipl import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^details/(?P<pk>[\d]+)/$', views.get_details, name='season_detail'),

    url(r'^login/$', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_view.LogoutView.as_view(), name='logout')
]
