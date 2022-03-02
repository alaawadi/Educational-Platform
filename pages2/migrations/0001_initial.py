# Generated by Django 3.1.14 on 2022-03-01 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields
import pages2.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=pages2.models.category_img)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=pages2.models.category_img)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('map', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=pages2.models.course_img)),
                ('title', models.CharField(max_length=100)),
                ('disc', models.TextField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages2.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=pages2.models.home_img)),
                ('title', models.CharField(max_length=100)),
                ('disc', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=pages2.models.teacher_img)),
                ('name', models.CharField(max_length=50)),
                ('work', models.CharField(max_length=50)),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('twiter', models.URLField()),
                ('github', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=pages2.models.video)),
                ('image', models.ImageField(upload_to=pages2.models.video_img)),
                ('title', models.CharField(max_length=100)),
                ('disc', models.TextField(blank=True, null=True)),
                ('code', models.FileField(blank=True, null=True, upload_to=pages2.models.code)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages2.course')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('img', models.ImageField(upload_to='images/procat')),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', froala_editor.fields.FroalaField()),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/blog')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upload_to', models.DateTimeField(auto_now=True)),
                ('vid_num', models.IntegerField(blank=True, null=True)),
                ('is_blog', models.BooleanField(default=False)),
                ('is_serv', models.BooleanField(default=False)),
                ('small_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('is_project', models.BooleanField(default=False)),
                ('user_slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('blog_Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages2.blog_category')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages2.course')),
                ('course_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pages2.category')),
                ('project_Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages2.project_category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=pages2.models.blog_img)),
                ('date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('smol_disc', models.TextField(max_length=200)),
                ('big_disc', models.TextField(max_length=100000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]