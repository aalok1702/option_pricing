from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns=[
    path("",views.index,name="myapp"),
    path("services",views.services,name="services"),
    path("two_step",views.two_step,name="two_step"),
    path("n_step",views.n_step,name="n_step"),
    path("black_scholes",views.black_scholes,name="black_scholes"),
]

