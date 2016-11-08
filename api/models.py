from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (AbstractUser, PermissionsMixin)
from .utils.auth_utils import app_secret_gen, app_key_gen
from django.utils import timezone
import logging
from utils.log import LoggerAdaptor
_logger = logging.getLogger(__name__)
from api.utils.datetime import to_seconds_from_datetime

class User(AbstractUser):
    """
    This is only for test purpose, users should override settings.AUTH_USER_MODEL

    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """
    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class App_Manager(models.Manager):

    logger = LoggerAdaptor('api.models.App_Manager>', _logger)

    def _create_app(self, user, app_name, **extra_fields):

        key, secret = app_key_gen(), app_secret_gen()

        _now = timezone.now()
        extra_fields['created_at'] = to_seconds_from_datetime(_now)#

        app = self.model(user=user, app_name=app_name, key=key, secret=secret, **extra_fields)

        app.save(using=self._db)
        return app

    def create(self, user=None, app_name=None, **extra_fields):
        return self._create_app(user, app_name, **extra_fields)


# Create your models here.
class App(models.Model):#, PermissionsMixin):

    key = models.CharField(verbose_name='key', db_column='key', max_length=128, unique=True, null=True)
    secret = models.CharField(verbose_name='secret', max_length=255, null=True)
    app_name = models.CharField(verbose_name='appname', db_column='appname', max_length=32, db_index=True, unique=True, null=True)
    user =  models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='app',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    auth_type = models.CharField(max_length=32,  null=True)
    callback_url = models.URLField(max_length=255, null=True )
    is_available = models.NullBooleanField(verbose_name='available', db_column='available', default=False,null=True)
    created_at = models.IntegerField(auto_created=True, db_index=True, default=None)
    latest_update_time = models.IntegerField(verbose_name='update_time', db_column='update_time', db_index=True, null=True )

    REQUIRED_FIELDS = ['key', 'secret', 'user', 'created_at']

    objects = App_Manager()

    class Meta:
        db_table = 'auth_app'

    class Admin:
        pass

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s : %s' % (self.app_name, self.key)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name.strip()


if __name__ == "__main__":
    pass
