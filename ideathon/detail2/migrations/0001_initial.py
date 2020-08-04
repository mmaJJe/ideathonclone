# Generated by Django 3.0.7 on 2020-07-28 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('user', models.CharField(max_length=20)),
                ('created_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='postImg')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail2.Post')),
            ],
        ),
    ]
