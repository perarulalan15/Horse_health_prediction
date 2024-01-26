from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.predictor,name='predictor'),
    path('submit',views.formInfo, name='result')
]