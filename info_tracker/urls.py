from api import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from api.router import DefaultDynamicQueryRouter as DefaultNestedRouter
# viewset
from api.viewsets import WebSiteViewSet, HeadlineViewSet, UserViewSet
from api.views import AppRegisterView, CreateRelView

from django.conf.urls import patterns, include, url
from django.contrib import admin

router = DefaultRouter()
nested_router = DefaultNestedRouter(is_method_attached=True)

nested_router.register(r'website', WebSiteViewSet)
nested_router.register(r'headline', HeadlineViewSet)
nested_router.register(r'user', UserViewSet)
router.register(r'subcribe', CreateRelView)

VERSION = '0.1.4'
HOST = '/api'
PREFIX = '^api/{v:}/'.format(v=VERSION)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'info_tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/{v:}/'.format(v=VERSION), include(nested_router.urls)),
    url(r'^api/{v:}/'.format(v=VERSION), include(router.urls)),
    url(r'^api/{v:}/auth/'.format(v=VERSION), include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/{v:}/register'.format(v=VERSION), AppRegisterView.as_view()),
    url(PREFIX, include('api.url')),
    # url(PREFIX, include('third_party.url')),
)
