from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from .utils.auth_utils import app_secret_gen, app_secret_coder, app_key_gen
from django.core.mail import send_mail
from django.utils import timezone
import logging
from utils.log import LoggerAdaptor
_logger = logging.getLogger(__name__)
from api.utils.datetime import to_seconds_from_datetime

class App_Manager(BaseUserManager):

    logger = LoggerAdaptor('api.models.App_Manager>', _logger)

    def _create_app(self, username=None, password=None, email=None, **extra_fields ):

        # print 'extra_fields: %s' % ', '.join((username, password, email, str(extra_fields),))
        if username is None or password is None:
            raise ValueError('username and password must be set to create account')

        if email is not None:
            email = self.normalize_email(email)

        app_key, app_secret = app_key_gen(username), app_secret_gen(password)
        extra_fields['app_key'] = app_key
        extra_fields['app_secret'] = app_secret

        _now = timezone.now()
        extra_fields['created_at'] = to_seconds_from_datetime(_now)#

        app = self.model(username=username, email=email, **extra_fields)

        if password is not None:
            app.set_password(password)

        app.save(using=self._db)# CHOSE DB backends
        return app

    def create(self, username=None, password=None, email=None, **extra_fields):
        return self._create_app(username, password, email, **extra_fields)


# Create your models here.
class App(models.Model):#, PermissionsMixin):

    # id = models.AutoField(auto_created=True, primary_key=True, null=False) # => autofield
    app_key = models.CharField(verbose_name='app_key', db_column='app_key', max_length=128, unique=True, null=True)
    app_name = models.CharField(verbose_name='appname', db_column='appname', max_length=32, db_index=True, unique=True, null=True)
    username = models.CharField(verbose_name='username', db_column='username', max_length=64, db_index=True, unique=True, null=False)
    auth_type = models.CharField(verbose_name='auth_type', max_length=32,  null=True)
    app_secret = models.CharField(verbose_name='app_secret', max_length=255, null=True)
    callback_url = models.URLField(verbose_name='callback_url', max_length=255, null=True )
    is_available = models.NullBooleanField(verbose_name='available', db_column='available', default=False,null=True)
    created_at = models.IntegerField(verbose_name='created_at', auto_created=True, db_index=True, null=True)
    email = models.EmailField(verbose_name='contact_email', db_column='contact_email',max_length=64, unique=True, db_index=True, default='', null=True)
    latest_update_time = models.IntegerField(verbose_name='update_time', db_column='update_time', db_index=True, null=True )
    token = models.CharField(verbose_name='token', max_length=255, unique=True, null=True)# important
    expire_date = models.DateField(verbose_name='expire_date', db_column='expire_date', db_index=True, null=True)
    password  = models.CharField(max_length=64, null=False)

    USERNAME_FIELD = 'app_name'
    REQUIRED_FIELDS = []

    objects = App_Manager()

    class Meta:
        db_table = 'auth_app'

    class Admin:
        pass

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s : %s' % (self.app_name, self.app_key)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


    def set_password(self, password):
        self.password = hash(password)

    def is_authenticated(self):
        return True

if __name__ == "__main__":
    pass
