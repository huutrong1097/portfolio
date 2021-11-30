from django.urls import path
from .views import index
# create path for a specific views
app_name = 'personal'

urlpatterns = [
    path('', index, name='index'),
]