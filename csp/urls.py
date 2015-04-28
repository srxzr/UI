from crowdsourcing import views
from crowdsourcing import views as api_views
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls) ),
    url(r'^api/v1/auth/login/$', views.Login.as_view()),
    url(r'^api/v1/auth/register/$', views.Registration.as_view()),
    url(r'^api/v1/auth/forgot-password/$',views.ForgotPassword.as_view()),
    url(r'^api/v1/auth/reset-password/(?P<reset_key>\w+)/(?P<enable>[0-1]*)/$',views.reset_password),
    url(r'^api/v1/auth/registration-successful',views.registration_successful),
    url(r'^api/v1/auth/logout/$', views.Logout.as_view()),
    url(r'^/account-activation/(?P<activation_key>\w+)/$', views.activate_account),
    url(r'^api/v1/auth/users/(?P<username>.+)/$', views.UserProfile.as_view()),
    url(r'^api/v1/auth/profile', views.UserProfile.as_view()),
    url(r'^api/v1/auth/ranking/$', views.RequesterRanking.as_view()),
    url(r'^worker$', views.worker),
    url(r'^requester', views.requester),
    url('^.*$', views.home, name='home'),
)


urlpatterns += staticfiles_urlpatterns()
