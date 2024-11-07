
from django.urls import path, include

from web.views import Dashboard


app_name = 'web'
urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]