# Generated by Django 3.2.2 on 2021-05-28 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traderecord', '0006_alter_stockrecords_graph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockrecords',
            name='graph',
            field=models.ImageField(blank=True, default='graph/default.jpg', upload_to='graph'),
        ),
    ]