import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Site_ports')
import django
django.setup()

from myapp.models import Work

Work.objects.create(
    title="Работа 1",
    short_description="Краткое описание работы 1",
    description="Подробное описание работы 1",
    image_url="https://example.com/image1.jpg"
)