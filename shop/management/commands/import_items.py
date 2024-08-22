# your_app/management/commands/import_items.py

import pandas as pd
from django.core.management.base import BaseCommand
from shop.models import Item
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Import items from an Excel file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']

        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading file: {e}'))
            return

        # Map your user profiles here
        user_map = {
            'eggy_': User.objects.get(username='eggy_'),
            'user1': User.objects.get(username='user1'),
            'user2': User.objects.get(username='user2'),
        }

        for index, row in df.iterrows():
            try:
                owner_username = row['owner']
                if owner_username not in user_map:
                    self.stdout.write(self.style.ERROR(f'User {owner_username} not found.'))
                    continue

                owner = user_map[owner_username]

                item, created = Item.objects.get_or_create(
                    name=row['name'],
                    defaults={
                        'year': row['year'],
                        'power': row['power'],
                        'fuel': row['fuel'],
                        'cabin_type': row['cabin_type'],
                        'description': row['description'],
                        'price': row['price'],
                        'phone_number': row['phone_number'],
                        'photo': row.get('photo', ''),  # Handle optional photo field
                        'owner': owner
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created item: {item.name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Item already exists: {item.name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing row {index}: {e}'))
