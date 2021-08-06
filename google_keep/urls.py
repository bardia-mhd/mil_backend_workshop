from rest_framework.routers import DefaultRouter

from google_keep import views_api

router = DefaultRouter()

router.register('keep-user', views_api.KeepUserViewSet)

urlpatterns = [

]

urlpatterns += router.urls
