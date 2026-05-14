from django.urls import path

from .views import (
    ProductListCreateView,
    ProductUpdateView
)

urlpatterns = [
    path('', ProductListCreateView.as_view()),
    path('<int:pk>/', ProductUpdateView.as_view()),
]