from django.urls import path
from . import views

urlpatterns = [
    path('',views.session_counter),
    path('destroy_session', views.destroy_session),
]

