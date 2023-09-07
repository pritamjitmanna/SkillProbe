
from django.urls import path

from . import views

urlpatterns=[
    path('dashboard/',views.dashboard),
    path('challenges/',views.challenge),
    path('test/',views.test_page),
    path('before_time/',views.before_time,name="BeforeTime"),
]
