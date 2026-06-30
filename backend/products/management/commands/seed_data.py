from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from faker import Faker
from common.utils import generate_slug
from categories.models import Category

fake = Faker()

User = get_user_model()


class Command(BaseCommand):

    help = "Seed ShopTrack database"

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.SUCCESS("Seeding database..."))

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

        categories = [
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

        for name in categories:
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