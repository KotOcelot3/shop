from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView
from .views import AllUserApiView, UserApiView, LoginAPIView, RegisterAPI, \
    AllVacanciesApiView, VacanciesIDView, UpdateUserAPI, UpdateVacanciesAPI

app_name = "product"

urlpatterns = [
    path('all-user/', AllUserApiView.as_view()),
    path('user<int:pk>/', UserApiView.as_view()),
    path('user-update<int:pk>/', UpdateUserAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    # path('login/', LoginAPIView.as_view()),
    path('logout/', TokenBlacklistView.as_view()),
    path('all-vacancies/', AllVacanciesApiView.as_view()),
    path('vacancies<int:pk>/', VacanciesIDView.as_view()),
    path('vacancies-update<int:pk>/', UpdateVacanciesAPI.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
