# Generated by Django 4.0.4 on 2022-07-04 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_contacto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacto',
        ),
        migrations.AddField(
            model_name='blog',
            name='titulo_nuevo',
            field=models.CharField(default='Blog', max_length=1000),
        ),
    ]