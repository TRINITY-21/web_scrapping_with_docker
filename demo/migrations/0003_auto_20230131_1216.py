# Generated by Django 3.2.16 on 2023-01-31 12:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Euro', max_length=10)),
                ('code', models.CharField(default='eur', max_length=10)),
                ('symbol', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('signed_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('signature_date', models.DateField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demo.country')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demo.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),

        migrations.AddField(
            model_name='loan',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demo.sector'),
        ),
    ]
