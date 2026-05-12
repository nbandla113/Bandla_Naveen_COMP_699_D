# apps/shared_space/urls.py

from django.urls import path
from .views import (
    create_space_view,
    join_space_view,
    exit_space_view,
    manage_space_view,
    user_spaces_view
)

urlpatterns = [
    path('create/', create_space_view, name='create_space'),
    path('join/', join_space_view, name='join_space'),
    path('exit/<int:space_id>/', exit_space_view, name='exit_space'),
    path('manage/<int:space_id>/', manage_space_view, name='manage_space'),
    path('my-spaces/', user_spaces_view, name='my_spaces'),
]