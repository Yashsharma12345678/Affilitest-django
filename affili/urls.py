from django.contrib import admin
from django.urls import path,include
from affili import views

urlpatterns = [
    path("",views.index,name='home'),
    # path('', views.redirect_analysis_view, name='redirect_analysis'),
]

