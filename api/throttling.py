__author__ = 'wangyi'
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class AnonRateThrottlePerMin(AnonRateThrottle):
    scope = 'anon/min'

class UserRateThrottlePerMin(UserRateThrottle):
    scope = 'user/min'