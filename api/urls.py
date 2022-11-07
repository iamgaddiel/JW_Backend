from django.urls import path

from .views import (
    api_index
)


app_name = 'api'

urlpatterns = [
    path('', api_index, name='index')
]