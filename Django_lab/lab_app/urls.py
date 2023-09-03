from django.urls import path
from lab_app import views

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
