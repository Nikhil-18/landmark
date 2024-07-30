from django.urls import path
from .views import (
    StoreListView, StoreDetailView, ItemListView, ItemDetailView,
    VendorListView, VendorDetailView, CategoryListView, CategoryDetailView,
    SaleListView, SaleDetailView
)

urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('stores/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('vendors/', VendorListView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('sales/', SaleListView.as_view(), name='sale-list'),
    path('sales/<int:pk>/', SaleDetailView.as_view(), name='sale-detail'),
]
