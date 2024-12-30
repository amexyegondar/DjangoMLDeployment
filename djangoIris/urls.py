from django.urls import path
from . import views

urlpatterns=[
    path('',views.prediction, name='predictor'),
    path('result',views.formInfo, name='result')
]