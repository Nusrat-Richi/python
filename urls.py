
from django.urls import path
from .views import productView
from . import views 
# Create your views here.
urlpatterns = {
    path("",views.index,name="index"),
    path('',productView.as_view(),name='product-op'),
    path("<int:id>/",productView.as_view(),name="product-op-with-id"),
}


