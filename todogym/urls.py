from rest_framework  import routers
from .api import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/todo',TodoViewSet,'todo')

urlpatterns = router.urls