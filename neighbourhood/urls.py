from django.urls import path
from . import views

urlpatterns=[

    path('', views.home, name='home'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('create_neighbourhood/', views.create_neighbourhood, name='create_neighbourhood'),
    path('single_neighbourhood/<str:name>/', views.single_neighbourhood, name='single_neighbourhood'),
    path('create_business/', views.create_business, name='create_business'),
    path('businesses/', views.businesses, name='businesses'),
]