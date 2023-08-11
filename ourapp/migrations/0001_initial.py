# Generated by Django 4.1.1 on 2023-05-21 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('det_img', models.ImageField(null=True, upload_to='detetcted_images')),
                ('detect', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Processed_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_img', models.ImageField(null=True, upload_to='extracted_images')),
                ('input_image_model', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detection_image', to='ourapp.input_image')),
            ],
        ),
    ]
