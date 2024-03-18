from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello_world),
    path('path/', views.get_path),
    path('form/', views.form),
    path('modelForm/', views.model_form),
    path('<str:dish>/', views.dish_desc),
    
]