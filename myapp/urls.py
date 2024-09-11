from django.urls import path
from . import views

urlpatterns = [
    # url for execute question 1 and 2
    path('create/', views.create_instance, name='create_instance'),
    # url for execute question 3
    path('create3/', views.create_instance_for_question_3, name='create_instance_for_question_3'),
]
