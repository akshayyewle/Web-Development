from django.urls import path, include
from application01 import views

urlpatterns = [
    path('^application01/', include(views.Model01_View)),
]