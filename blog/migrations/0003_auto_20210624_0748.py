# Generated by Django 3.1.7 on 2021-06-24 07:48

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210623_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='tabs',
            field=wagtail.core.fields.StreamField([('legal', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock())])), ('team', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('children', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('role', wagtail.core.blocks.CharBlock()), ('project_description', wagtail.core.blocks.CharBlock()), ('personal_description', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('twitter', wagtail.core.blocks.URLBlock()), ('linkedin', wagtail.core.blocks.URLBlock()), ('instagram', wagtail.core.blocks.URLBlock()), ('github', wagtail.core.blocks.URLBlock()), ('youtube', wagtail.core.blocks.URLBlock())])))])), ('clients', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('children', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('url', wagtail.core.blocks.URLBlock())])))])), ('contact_us', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('subject_prefix', wagtail.core.blocks.CharBlock())])), ('appointment', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock())]))]),
        ),
    ]
