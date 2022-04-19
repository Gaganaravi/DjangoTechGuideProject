from django.urls import path, include
from . import views
urlpatterns =[
    path('',views.index),
    path('login/', views.loginaction),
    path('signup/', views.signaction),
    path('feed/', views.feed),
    path('add/', views.add),
    path('feed/',views.feed ),
    path('aboutus/', views.aboutus),
    path('profile/', views.profile),
    
]