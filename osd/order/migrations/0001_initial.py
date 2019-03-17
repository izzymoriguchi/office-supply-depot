# Generated by Django 2.1.7 on 2019-03-17 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Order Total')),
                ('ship_address', models.CharField(max_length=250)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Discounted Amount')),
                ('freight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Delivery Cost')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tax')),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['-order_date'],
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Product Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
            options={
                'db_table': 'OrderDetail',
            },
        ),
    ]
