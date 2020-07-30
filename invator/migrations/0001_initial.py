# Generated by Django 3.0.8 on 2020-07-30 16:21

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
            name='Invator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, verbose_name='name')),
                ('Workdone', models.CharField(max_length=255)),
                ('Amount', models.CharField(max_length=255000000)),
                ('Hours', models.CharField(max_length=2500000)),
                ('HourAmount', models.CharField(max_length=255000000)),
                ('ContractAmount', models.CharField(max_length=255000000)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.CharField(blank=True, max_length=30, null=True)),
                ('total', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('to_full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('to_address', models.CharField(blank=True, max_length=500, null=True)),
                ('to_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('from_full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, max_length=15, null=True)),
                ('from_web_address', models.CharField(blank=True, max_length=15, null=True)),
                ('tax', models.CharField(blank=True, max_length=15, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=15, null=True)),
                ('terms', models.CharField(blank=True, max_length=300, null=True)),
                ('from_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('transactions', models.ManyToManyField(to='invator.Transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]