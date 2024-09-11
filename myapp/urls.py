from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_instance, name='create_instance'),
    path('create3/', views.create_instance_for_question_3, name='create_instance_for_question_3'),
]
