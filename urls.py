from django.conf.urls import patterns, include, url
from django.contrib import admin
from myEfforts import views
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^myefforts/$', views.index, name='index'),
    url(r'^sign-up/$', views.signup, name='sign-up'),
    url(r'^register/$',views.register, name='register'),
    url(r'^register/ngo/(?P<email>[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4}))/$',views.regNgo),
    url(r'^register/user/(?P<email>[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4}))/$',views.regCustomer),
    url(r'^register/success/$',views.success),
    url(r'work/$',views.work,name='work'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'login/$','login', { 'template_name':'signin.html' },
        name='login'),
)

