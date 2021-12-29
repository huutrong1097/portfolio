from django.urls import include, path
from rest_framework import routers
from . import views
app_name = 'personal'
router = routers.DefaultRouter()
router.register(r'about', views.AboutViewSet)
router.register(r'skill', views.SkillViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]