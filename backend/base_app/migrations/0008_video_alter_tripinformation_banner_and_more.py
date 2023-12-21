# Generated by Django 5.0 on 2023-12-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0007_alter_tripinformation_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
            ],
        ),
        migrations.AlterField(
            model_name='tripinformation',
            name='banner',
            field=models.ImageField(upload_to='trip_banners/'),
        ),
        migrations.AlterField(
            model_name='tripinformation',
            name='end_date_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tripinformation',
            name='start_date_time',
            field=models.DateField(),
        ),
    ]
