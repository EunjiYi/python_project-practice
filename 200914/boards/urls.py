from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('index/', views.index, name='idx'),
    path('vr/<str:name>/', views.variable, name='vari'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('upd/<int:id>/', views.update, name="update"),
    path('del/<int:id>/', views.delete, name="del"),
]
