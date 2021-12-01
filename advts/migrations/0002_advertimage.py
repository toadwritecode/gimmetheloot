# Generated by Django 3.2.9 on 2021-12-01 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Фотография')),
                ('advert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='advts.advert', verbose_name='Объявление')),
            ],
        ),
    ]
