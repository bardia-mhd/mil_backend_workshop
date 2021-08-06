from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from google_keep.models import KeepUser
from google_keep.serializers import KeepUserSerializer


class KeepUserViewSet(ModelViewSet):
    serializer_class = KeepUserSerializer
    queryset = KeepUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

