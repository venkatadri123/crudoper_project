from django.urls import path
from app_crudoper import views

urlpatterns = [
    path('', views.show, name='show'),
    path('show/', views.show, name='show'),
    path('view/<int:id>', views.view, name='view'),
    path('register/', views.register, name='register'),
    path('image_update/<int:id>', views.image_update, name='image_update'),
    path('update/<int:id>/<str:user>', views.update, name='update'),
    path('delete/<int:id>/<str:username>/', views.destro, name='destro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
