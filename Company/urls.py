
from django.urls import path,include
from . import views


challenges=[
    path('create/',views.create_challenge,name='CreateChallenge'),
    path('create/page/',views.page_challenge,name='PageChallenge'),
    path('create/mcq/',views.add_mcq,name='AddMCQ'),
    path('create/coding/',views.add_coding,name='AddCoding'),
]


urlpatterns=[
    path('dashboard/',views.dashboard),
    path('challenge/',include(challenges)),
]
