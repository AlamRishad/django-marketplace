from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.jobsFeed, name='jobsFeed'),
    path('jobs/<id>', views.jobDetails, name='jobsFeed'),
    path('bid/<freelancerId>/<jobId>', views.bid, name='bid'),
    path('reg/freelancer', views.freelancerRegister, name='freelancerRegister'),
    path('reg/client', views.clientRegister, name='clientRegister'),
    path('login/client/', views.clientLogin, name='clientLogin'),
    path('logout/', views.logoutUser, name='clientLogin'),
]