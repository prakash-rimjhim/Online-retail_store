# Generated by Django 2.2.25 on 2021-12-12 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200, null=True, unique=True)),
                ('productId', models.UUIDField(default=uuid.uuid4, null=True)),
                ('availableQuantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('productName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail_store.Product')),
            ],
        ),
    ]
