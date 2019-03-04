# Generated by Django 2.1.7 on 2019-02-25 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('housing_app', '0002_auto_20190212_0511'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('is_authenticated', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('favorites', models.ManyToManyField(to='housing_app.Apartment')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
