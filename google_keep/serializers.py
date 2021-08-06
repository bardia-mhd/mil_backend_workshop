from rest_framework.serializers import ModelSerializer

from google_keep.models import KeepUser


class KeepUserSerializer(ModelSerializer):
    class Meta:
        model = KeepUser
        fields = (
            'id', 'first_name', 'last_name', 'email', 'password'
        )
        read_only_fields = ('id',)
