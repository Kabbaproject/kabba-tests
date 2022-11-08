from django.urls import path
from . import views



urlpatterns = [
    path("login/",views.loginPage, name="login"),
    path("logout/",views.logOut, name="logout"),
    path("",views.home, name="home"),
    path("product/",views.products, name="product"),
    path("customer/",views.customer,name="customer"),
    # path("customer/<str:pk>/",views.customer, name="single_customer"),
    path("service/",views.service, name="service"),
    path("create_customer/",views.create_customer, name="create_customer"),
    path("create_service/",views.create_service, name="create_service"),
    path("create_product/",views.create_product, name="create_product"),
    path("update_customer/<str:pk>/",views.update_customer, name="update_customer"),
    path("update_service/<str:pk>/",views.update_service, name="update_service"),
    path("update_product/<str:pk>/",views.update_product, name="update_product"),
    path("delete_customer/<str:pk>/",views.delete_customer, name="delete_customer"),
    path("delete_service/<str:pk>/",views.delete_service, name="delete_service"),
    path("delete_product/<str:pk>/",views.delete_product, name="delete_product"),
    path("summary/<str:pk>/",views.summary, name="summary"),
    
    
]