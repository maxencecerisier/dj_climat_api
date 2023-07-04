# Generated by Django 4.2.2 on 2023-06-10 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('climate', '0004_serviceprovider_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Pending', max_length=255)),
                ('price_estimate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(default='Quote Description')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climate.service')),
                ('climate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climate.serviceprovider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]