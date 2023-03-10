# Generated by Django 3.2.9 on 2023-03-06 11:06

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('txn_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email_or_mobile', models.TextField(default='')),
                ('otp', models.CharField(max_length=10)),
                ('expire_at', models.DateTimeField()),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'otp',
            },
        ),
        migrations.CreateModel(
            name='PasswordResetToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('token', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'passwordresettokens',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.CharField(editable=False, max_length=256, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.", regex='^\\d{9,10}$')], verbose_name='Mobile No')),
                ('first_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Last Name')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=8, verbose_name='Gender')),
                ('profile_picture', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics', verbose_name='Profile Picture')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address_line_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address 1')),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address 2')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='City')),
                ('is_blocked', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_mobile_verified', models.BooleanField(default=False, verbose_name='Mobile Verified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
        ),
    ]