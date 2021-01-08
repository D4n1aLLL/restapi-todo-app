from TodoAPI.viewsets import TaskViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task',TaskViewset)