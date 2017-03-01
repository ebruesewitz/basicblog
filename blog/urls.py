from django.conf.urls import url
from . import views

urlpatterns = [
    # home page listing all posts. nothing added to url. linking to a function-based view
    url(r'^$', views.post_list, name='post_list'),
    # specific post page with url that is defined by the post's pk (must be at least 1 digit)
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # link to the post creation page (add new to the end of url)
    url(r'^post/new/$', views.post_new, name = 'post_new'),
    # link to the post edit page. similar to the creation one. url contains pk for post followed by /edit
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]