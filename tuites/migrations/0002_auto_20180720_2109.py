# Generated by Django 2.0.7 on 2018-07-21 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tuites', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tuite',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterField(
            model_name='tuite',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuites', to=settings.AUTH_USER_MODEL),
        ),
    ]
