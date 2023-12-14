from django.urls import path
from api import views

urlpatterns = [
    path('', views.Predict.as_view(), name="texts"),
]