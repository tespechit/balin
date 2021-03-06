from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from balin.auth_balin.views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView
)


# Routes of contrib.auth
urlpatterns = patterns(
    '',
    url(r'users/$', UserListView.as_view(), name='list'),
    url(r'user/create/$', UserCreateView.as_view(), name='create'),
    url(r'user/(?P<pk>\d+)/update/$',
        UserUpdateView.as_view(), name='update'),
    url(r'user/(?P<pk>\d+)/delete/$',
        UserDeleteView.as_view(), name='delete'),

    url(r'^login/$', auth_views.login,
        {'template_name': 'registration/login.html'},
        name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/login/'}, name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^password_change/done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
        name='password_reset'),
    url(r'^password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
)
