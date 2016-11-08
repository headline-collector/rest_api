__author__ = 'wangyi'

from api.models import App
from rest_framework import serializers
from django.contrib.auth import get_user_model
from third_party.models import User

class App_Serializer(serializers.ModelSerializer):

    def create(self, validated_data):
        app = App.objects.create(user=validated_data['user'],
                                 app_name=validated_data['app_name'],)
        return app

    class Meta:
        model = App
        fields = '__all__'
