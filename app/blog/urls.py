from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    path('comment/', views.CommentCreateView.as_view()),
    path('comment/<int:pk>/', views.CommentDeleteView.as_view()),

]
