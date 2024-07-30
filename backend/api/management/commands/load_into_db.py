import csv
import os.path
from django.core.management.base import BaseCommand
from api.models import Store, Item, Vendor, Category, Sale
from django.conf import settings

default_data_path = os.path.join(settings.BASE_DIR.parent, 'assignment', 'sample.csv')
default_data_path = os.path.join(settings.BASE_DIR.parent, 'assignment', 'sample_big.csv')

class Command(BaseCommand):
    help = '''
        Load CSV data into the database
    '''

    def add_arguments(self, parser):
        parser.add_argument('--data_path', type=str, default=default_data_path, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        data_path = kwargs['data_path']
        with open(data_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                store, _ = Store.objects.get_or_create(
                    store_number=row['Store Number'],
                    store_name=row['store_name'],
                    address=row['Address'],
                    city=row['City'],
                    zip_code=row['Zip Code'],
                    store_location=row['Store Location'],
                    county_number=row['County Number'],
                    county=row['County'],
                )
                item, _ = Item.objects.get_or_create(
                    item_number=row['Item Number'],
                    item_desc=row['item_desc'],
                    pack=row['Pack'],
                    bottle_volume_ml=row['Bottle Volume (ml)'].replace(',', ''),
                    state_bottle_cost=row['State Bottle Cost'],
                    state_bottle_retail=row['State Bottle Retail'],
                )
                vendor, _ = Vendor.objects.get_or_create(
                    vendor_number=row['Vendor Number'],
                    vendor_name=row['vendor_name'],
                )
                category, _ = Category.objects.get_or_create(
                    category_number=row.get('Category'),
                    category_name=row['category_name'],
                )
                Sale.objects.create(
                    invoice_item_number=row['Invoice/Item Number'],
                    date=row['Date'],
                    store=store,
                    item=item,
                    vendor=vendor,
                    category=category,
                    bottles_sold=row['Bottles Sold'],
                    sale_dollars=row['Sale (Dollars)'].replace(',', ''),
                    volume_sold_liters=row['Volume Sold (Liters)'],
                    volume_sold_gallons=row['Volume Sold (Gallons)'],
                )
