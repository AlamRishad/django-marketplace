from django.urls import path
from . import views



urlpatterns = [
    path('', views.firstpage, name='firstpage'),
    path('home/', views.home, name='home'),
    path('jobs/', views.jobsFeed, name='jobsFeed'),
    path('jobs/<id>', views.jobDetails, name='jobsFeed'),
    path('jobs/bid/<jobId>', views.bid, name='bid'),
    path('job/create', views.jobCreate, name='jobcreate'),
    path('reg/freelancer', views.freelancerRegister, name='freelancerRegister'),
    path('reg/client', views.clientRegister, name='clientRegister'),
    path('login/client/', views.clientLogin, name='clientLogin'),
    path('login/freelancer/', views.freelancerLogin, name='freelancerLogin'),
    path('logout/', views.logoutUser, name='clientLogin'),
    path('blog/create', views.blogCreate, name='blogCreate'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<blogid>', views.blogDetail, name='blogDetail'),
    path('award/<jobId>/<freelancerId>/<biddingId>', views.award, name='award'),
]

