# Generated by Django 4.0.5 on 2022-07-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0010_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click linka bove to view details', max_length=255),
        ),
    ]