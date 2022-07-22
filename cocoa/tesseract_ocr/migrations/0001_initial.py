# Generated by Django 2.2.4 on 2020-10-23 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('internal_reference', models.CharField(editable=False, max_length=100, verbose_name='Internal Reference')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='OCR_image/input/', verbose_name='Input Image')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
            ],
            options={
                'verbose_name': 'ImageFile',
                'verbose_name_plural': 'ImageFiles',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='OCRText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='OCR text')),
                ('lang', models.TextField(default='EN', verbose_name='Language')),
                ('execution_time', models.IntegerField(editable=False, null=True, verbose_name='Execution Time')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tesseract_ocr.ImageFile')),
            ],
            options={
                'verbose_name': 'OCRText',
                'verbose_name_plural': 'OCRTexts',
                'ordering': ['id'],
            },
        ),
    ]
