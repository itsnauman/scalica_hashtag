from django.conf.urls import include, url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^stream/(?P<user_id>[0-9]+)/$', views.stream, name='stream'),
    url(r'^post/$', views.post, name='post'),
    url(r'^follow/$', views.follow, name='follow'),
    url(r'^register/$', views.register, name='register'),
    url(r'^search/(?P<hashtag>[\w\-]+)/$', views.stream_hashtag_with_sentiment, name='hashtag_sentiment'),
    url('^', include('django.contrib.auth.urls'))
]


'''Mir
Need to create following view(s):
1. A view that will allow a user to search for posts for a
given topic/hashtag. For each post in the view, it should also
display the sentiment type of that post.
'''
