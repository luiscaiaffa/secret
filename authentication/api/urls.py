from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views

urlpatterns = [
    path('token/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),
    path('verify/', verify_jwt_token),
    path('basea/<str:cpf>/', views.BaseA.as_view()),
    path('baseb/<str:cpf>/', views.BaseB.as_view()),
    path('basec/<str:cpf>/', views.BaseC.as_view()),
]
