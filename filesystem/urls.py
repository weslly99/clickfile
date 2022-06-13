from django.urls import path
from . import views

urlpatterns = [
    path('', views.DirectoryList.as_view()),
    path('<int:pk>', views.DirectoryDetail.as_view()),
    path('files/<int:pk>/', views.FileDetail.as_view()),
    path('files/', views.FileList.as_view()),
]