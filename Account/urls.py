from django.urls import path
from rest_framework.authtoken import views

from Account.views import UserListView

app_name = "Account"

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
]