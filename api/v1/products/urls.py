from django.urls import path

from api.v1.products import views


urlpatterns = [
    path('', views.ProductView),
    path('create-product/', views.create_product),
    path('edit-product/', views.edit_product),
]
