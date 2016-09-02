from django.conf.urls import include, url
from django.contrib import admin
from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', 'app.views.login_view'),
    url(r'^signup', 'app.views.sign_up'),
    url(r'^homepage/', 'app.views.homepage'),
    # url(r'^signout/$', 'app.views.signout_view'),
]
