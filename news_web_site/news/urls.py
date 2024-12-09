from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsAllView.as_view(), name='news_home'),
    path('create', views.NewsCreateView.as_view(), name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
]
