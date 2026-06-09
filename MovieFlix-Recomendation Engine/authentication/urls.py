from django.urls import path,include

from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', signupView.as_view(), name='signup')
]
