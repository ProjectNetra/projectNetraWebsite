# Generated by Django 3.1.7 on 2021-07-05 07:14

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('blog', '0011_auto_20210629_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='player_embed',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='tabs',
            field=wagtail.core.fields.StreamField([('legal', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock())])), ('team', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('children', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('role', wagtail.core.blocks.CharBlock()), ('project_description', wagtail.core.blocks.CharBlock()), ('personal_description', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('twitter', wagtail.core.blocks.URLBlock(required=False)), ('linkedin', wagtail.core.blocks.URLBlock(required=False)), ('instagram', wagtail.core.blocks.URLBlock(required=False)), ('github', wagtail.core.blocks.URLBlock(required=False)), ('youtube', wagtail.core.blocks.URLBlock(required=False))])))])), ('contact_us', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('subject_prefix', wagtail.core.blocks.CharBlock())])), ('appointment', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock())]))]),
        ),
        migrations.DeleteModel(
            name='BlogCategoryIndexPage',
        ),
    ]
