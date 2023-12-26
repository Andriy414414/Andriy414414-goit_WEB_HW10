from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>', views.main, name="root_paginate"),
    path('author/<str:_id>', views.about, name="about"),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/add_quote', views.add_quote, name="add_quote"),
    path('accounts/add_author', views.add_author, name="add_author"),


]