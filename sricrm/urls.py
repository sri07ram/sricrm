from django.urls import path,include
from sricrm.views.registerview import UserView
from sricrm.views.companyview import CompanyView
from sricrm.views.organizationview import OrganizationView
from sricrm.views.otpgenerateview import GenerateOTPView
from sricrm.views.otpverifyview import OTPVerifyAPIView
from sricrm.views.profileview import ProfileView,ProfileViewByID
from sricrm.views.loginview import LoginView

from knox import views as knox_views

urlpatterns=[
    path('3-User Register/', UserView.as_view(), name='User Register'),
    path('4-Organization Register/', OrganizationView.as_view(), name='Organization Register'),
    path('5-Company Register/', CompanyView.as_view(), name='Company Register'),
    path('1-Generate-OTP/', GenerateOTPView.as_view(), name='Generate-OTP'),
    path('2-Verify-OTP/', OTPVerifyAPIView.as_view()),
    path('6-Login/', LoginView.as_view(), name='knox_login'),
    path('7-Profile/', ProfileView.as_view(), name='User-Profile'),
    path('7-Profile/<str:profile_id>/', ProfileViewByID.as_view(), name='universal-profile')
]
