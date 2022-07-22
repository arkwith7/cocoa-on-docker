# Generated by Django 3.2.6 on 2022-07-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesseract_ocr', '0003_auto_20210102_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessregistrationocrtext',
            name='image',
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ocrtext',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='BusinessRegistrationImageFile',
        ),
        migrations.DeleteModel(
            name='BusinessRegistrationOCRText',
        ),
    ]
