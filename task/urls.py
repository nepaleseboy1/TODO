from django.urls import path
from .import views

urlpatterns = [ 
    path ('', views.home, name="home"),
    path('update-task/<str:pk>/', views.updateTask , name='update_task' ),
    path('delete-task/<str:pk>/', views.deleteTask , name='delete_task' ),

]