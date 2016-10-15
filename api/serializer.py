__author__ = 'wangyi'

from api.models import App
from rest_framework import serializers
from django.contrib.auth import get_user_model
from third_party.models import User

class App_Serializer(serializers.ModelSerializer):

    def create(self, validated_data):
        UserModel = get_user_model()
        app = App.objects.create(username=validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['email'])
        user = User(username=validated_data['username'], auth_id=app)
        user.save(using=self._db)
        return user

    class Meta:
        model = App
        fields = '__all__'
