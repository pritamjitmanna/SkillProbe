from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('signin/',views.signIn,name="signin"),
    path('signup/',views.signUp,name="signup"),
]