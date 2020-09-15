from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('detail/<str:id>/', views.detail, name='detail'),
    path('edit/<str:pk>/', views.update, name='update'),
    path('del/<pk>', views.delete, name='delete'), #str 생략가능 디폴트가 str임
]
