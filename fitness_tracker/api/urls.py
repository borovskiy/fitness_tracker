from rest_framework import routers
from .views import UserActiveViewSet

router = routers.SimpleRouter()
router.register('add_activ', UserActiveViewSet, basename='user')
urlpatterns = router.urls