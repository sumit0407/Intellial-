from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [

    path("",views.Homepage,name="homepage"),

    path("Customerpage/",views.Customers,name="customerpage"),

    path("addcust/",views.Addcust,name='addcustomer'),

    path("prod/",views.Productssss,name='prod'),

    path("productdata",views.Productadddata,name='productdata'),

    path("addorder/",views.Addorderss,name='addorderss'),

    path("succes/",views.successpage,name='s'),

    path("Orderpage/",views.Orderpage,name='orderpage'),

    path("serch/",views.Serch,name='serch'),

    path("Editpage/<int:pk>/",views.Editpage,name='editpage'),

    path("Editdatatable/<int:pk>/",views.Editdatatable,name='editdatatable'),

    path("Delete/<int:pk>/",views.Deletedata,name='delete'),
]