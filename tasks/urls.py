from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')
urlpatterns = router.urls