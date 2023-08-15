from django.urls import path
from .views import check_if_email_hacked

urlpatterns = [
    path('<str:email>/', check_if_email_hacked),
]
