"""Mark_LEE_assignment2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', include('schedule2.urls')),
    path('', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('searchdestination/', views.searchdestination, name='searchdestination'),
    path('searchdestination/searcheddesti/', views.searcheddesti, name='searcheddesti'),
    path('searchdestination/searcheddesti/book/<int:id>', views.bookdestination, name='bookdestination'),
    path('searchdestination/searcheddesti/book/addrecord/<int:id>', views.addrecord, name='addrecord'),
    path('search/searched/', views.searched, name='serached'),
    path('search/searched/book/<int:id>', views.book, name='book'),
    path('search/searched/book/addrecord/<int:id>', views.addrecord, name='addrecord'),
    path('search/searched/book/addrecord/bookedflight', views.bookedflight, name='bookedflight'),
    path('customer/', views.addcustomer, name='customer'),
    path('customer/add_customer_detail/', views.add_customer_detail, name='add_customer_detail'),
    path('customerlist/', views.customerList, name='customerList'),
    path('reference/', views.reference, name='reference'),
    path('reference/searchreference/', views.searchreference, name='searchreference'),
    path('cancelation/', views.cancelation, name='cancelation'),
    path('cancelation/confirmcancelation/', views.confirmcancelation, name='confirmcancelation'),
    path('name/', views.name, name='name'),
    path('name/searchname/', views.searchname, name='searchname'),
]
