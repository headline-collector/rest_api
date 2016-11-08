from __future__ import unicode_literals

__author__ = 'wangyi'

from rest_framework.viewsets import ViewSetMixin
from views import WebSiteViewRouter, HeadlineViewRouter, UserViewRouter, UserWebsiteViewRouter
from third_party.models import WebSite, Headline, User
from third_party.serializer import WebSiteSerializer, HeadlineSerializer, UserSerializer

class WebSiteViewSet(ViewSetMixin,
                    WebSiteViewRouter):

    verbose_key = 'website'
    prefix_abbr = 'ws'

    affiliates = ['headline',]

class HeadlineViewSet(ViewSetMixin,
                    HeadlineViewRouter):

    verbose_key = 'headline'
    prefix_abbr = 'hl'

class UserViewSet(ViewSetMixin,
                  UserViewRouter):

    verbose_key = 'user'
    prefix_abbr = 'ur'


class UserWebsiteViewSet(ViewSetMixin,
                         UserWebsiteViewRouter):

    verbose_key = 'rel'
    prefix_abbr = 'uw'