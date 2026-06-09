from django.urls import path,include

from recomendationchamber.views import homepage

urlpatterns = [
    path('home/',homepage.as_view(),name='home'),
]