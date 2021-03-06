# Generated by Django 3.1.7 on 2021-06-27 07:40

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('blog', '0007_auto_20210625_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='LegalPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('description', wagtail.core.fields.RichTextField()),
                ('tabs', wagtail.core.fields.StreamField([('legal', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock())]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='thumbnail',
        ),
    ]
