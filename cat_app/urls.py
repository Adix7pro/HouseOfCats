from django.urls import path
from .views import (PostListView,
                    PostDeleteView,
                    PostUpdateView,
                    PostCreateView,
                    PostDetailView)
app_name = "posts"
urlpatterns = [
    path('',PostListView.as_view(),name='list'),
    path('<int:pk>/delete',PostDeleteView.as_view(),name='delete'),
    path('<int:pk>/update',PostUpdateView.as_view(),name='update'),
    path('create',PostCreateView.as_view(),name='create'),
    path('<int:pk>/',PostDetailView.as_view(),name='detail'),
]