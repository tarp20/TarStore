# Generated by Django 3.1.2 on 2020-10-29 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='name')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Diagonal')),
                ('display_type', models.CharField(max_length=255, verbose_name='Display type')),
                ('resolution', models.CharField(max_length=255, verbose_name='Screen resolution')),
                ('accum_volume', models.CharField(max_length=255, verbose_name='Battery volume')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('sd', models.BooleanField(default=True, verbose_name='SD')),
                ('sd_volume_max', models.CharField(blank=True, max_length=255, null=True, verbose_name='Maximum built-in memory')),
                ('main_cam_mp', models.CharField(max_length=255, verbose_name='Main camera')),
                ('frontal_cam_mp', models.CharField(max_length=255, verbose_name='Front-camera')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='name')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Diagonal')),
                ('display_type', models.CharField(max_length=255, verbose_name='Type od dyspley')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='CPU frequency')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('video', models.CharField(max_length=255, verbose_name='Videocard')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Battery life')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
