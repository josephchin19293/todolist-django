from django.urls import path
from . import views

urlpatterns = [
    path('', views.todaytodos, name='today'),
    path('remove/<int:todo_id>/', views.remove, name='remove')
    #
]
