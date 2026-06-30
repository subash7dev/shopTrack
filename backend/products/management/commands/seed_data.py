from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from faker import Faker

from common.utils import generate_slug
from categories.models import Category
from products.models import Product

fake = Faker()

User = get_user_model()


class Command(BaseCommand):

    help = "Seed ShopTrack database"

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.SUCCESS("Seeding database..."))

        # Create Admin
        admin, created = User.objects.get_or_create(
            email="admin@shoptrack.com",
            defaults={
                "name": "Administrator",
                "is_staff": True,
                "is_superuser": True,
            },
        )

        if created:
            admin.set_password("Admin@123")
            admin.save()

            self.stdout.write(
                self.style.SUCCESS("Admin user created.")
            )

        # Create Categories
        category_names = [
            "Electronics",
            "Fashion",
            "Books",
            "Sports",
            "Furniture",
            "Beauty",
            "Groceries",
            "Toys",
            "Automotive",
            "Accessories",
        ]

        for name in category_names:

            Category.objects.get_or_create(
                slug=generate_slug(name),
                defaults={
                    "name": name,
                    "slug": generate_slug(name),
                    "created_by": admin,
                    "updated_by": admin,
                },
            )

        self.stdout.write(
            self.style.SUCCESS("Categories created.")
        )

        # Fetch categories from DB
        categories = list(Category.objects.all())

        # Create Products
        for _ in range(100):

            name = fake.unique.word().title()

            Product.objects.get_or_create(
                slug=generate_slug(name),
                defaults={
                    "name": name,
                    "slug": generate_slug(name),
                    "description": fake.sentence(),
                    "price": fake.pydecimal(
                        left_digits=4,
                        right_digits=2,
                        positive=True,
                    ),
                    "stock_quantity": fake.random_int(
                        min=1,
                        max=150,
                    ),
                    "category": fake.random_element(categories),
                    "created_by": admin,
                    "updated_by": admin,
                },
            )

        self.stdout.write(
            self.style.SUCCESS("100 Products created.")
        )

        self.stdout.write(
            self.style.SUCCESS("Database seeded successfully.")
        )