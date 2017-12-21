from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


from . import views

app_name = 'molecule'

urlpatterns = [
    url(r'^$', views.index, name='index'),        # start with just views.index
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^create_account/', views.create_account, name='create_account'),
    url(r'^groups/', views.groups, name='groups'),
    url(r'^messages/', views.messages, name='messages'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^admin/', admin.site.urls),
]