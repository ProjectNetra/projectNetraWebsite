# Generated by Django 3.1.7 on 2021-06-24 07:50

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210624_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='description',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
    ]
