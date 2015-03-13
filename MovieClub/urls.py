from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'newsfeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'newsfeed.views.login_user'),
    url(r'^profile/', 'newsfeed.views.user_profile'),
    url(r'^friends/', 'newsfeed.views.friends'),
    url(r'^home/', 'newsfeed.views.home'),
    url(r'^edit_profile_form/', 'newsfeed.views.edit_profile_form'),
    url(r'^friend_profile/', 'newsfeed.views.friend_profile'),
    url(r'^kicks_list/', 'newsfeed.views.kicks_list'),
    url(r'^add_kick_form/', 'newsfeed.views.add_kick_form'),
    url(r'^kick_profile/', 'newsfeed.views.kick_profile'),
    url(r'^season/', 'newsfeed.views.season'),
    # url(r'^accounts/login/?next=/profile/', 'newsfeed.views.user_profile'),
  
    
)
