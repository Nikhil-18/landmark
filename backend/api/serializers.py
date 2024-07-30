from rest_framework import serializers
from .models import Store, Item, Vendor, Category, Sale

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    item = ItemSerializer()
    vendor = VendorSerializer()
    category = CategorySerializer()

    class Meta:
        model = Sale
        fields = '__all__'
