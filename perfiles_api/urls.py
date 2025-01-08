from django.urls import path

from perfiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]