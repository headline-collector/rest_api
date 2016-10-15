__author__ = 'wangyi'


from django.conf.urls import url

from .views import UserWebsiteViewRouter, CreateRelView
#(<?P<username>[\w\d][\w\d_]*)/(?P<website_name>[\w\d][\w\d_]*)
urlpatterns = [
    url(r'subcribe/list/(?P<username>[\w\d][\w\d_]*)/$', UserWebsiteViewRouter.as_view()),
    # url(r'subcribe/create/(<?P<username>[\w\d][\w\d_]*)/(?P<website_name>[\w\d][\w\d_]*)/$', CreateRelView.as_view({'post': 'create'})),
    # url(r'subcribe/remove/(<?P<username>[\w\d][\w\d_]*)/(?P<website_name>[\w\d][\w\d_]*)/$', CreateRelView.as_view({'delete': 'remove'})),
]