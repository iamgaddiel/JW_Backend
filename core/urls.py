from django.urls import path

from .views import (
    Index,
    JerseyStoreView,
    JerseyDetailView
)


app_name = 'core'


urlpatterns = [
    path(
        '',
        Index.as_view(),
        name='index'
    ),
    path(
        'store/<str:category>/',
        JerseyStoreView.as_view(),
        name='store'
    ),
    path(
        'jersey/<str:category>/<uuid:pk>/',
        JerseyDetailView.as_view(),
        name='jersey_detail'
    ),
]
