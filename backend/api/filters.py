import django_filters
from .models import Sale

class SaleFilter(django_filters.FilterSet):
    class Meta:
        model = Sale
        fields = {
            'store__store_name': ['exact', 'icontains'],
            'store__city': ['exact'],
            'item__item_desc': ['exact', 'icontains'],
            'vendor__vendor_name': ['exact', 'icontains'],
            'category__category_name': ['exact', 'icontains'],
            'date': ['exact', 'year__exact', 'year__gte', 'year__lte'],
            'bottles_sold': ['exact', 'gte', 'lte'],
            'sale_dollars': ['exact', 'gte', 'lte'],
        }
