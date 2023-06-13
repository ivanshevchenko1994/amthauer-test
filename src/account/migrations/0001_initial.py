# Generated by Django 4.1.7 on 2023-04-10 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated date')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('domain', models.CharField(blank=True, max_length=255, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('external_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('img_url', models.CharField(blank=True, max_length=255, null=True)),
                ('matching_ready', models.BooleanField(blank=True, null=True)),
                ('relevance_rate_threshold', models.IntegerField(blank=True, null=True)),
                ('slack_access_token', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('logo_url', models.CharField(blank=True, max_length=255, null=True)),
                ('landing_copy', models.CharField(blank=True, max_length=2048, null=True)),
                ('landing_title', models.CharField(blank=True, max_length=512, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Community',
                'verbose_name_plural': 'Communities',
                'db_table': 'community',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated date')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(db_index=True, max_length=255, null=True, verbose_name='First name')),
                ('last_name', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Last name')),
                ('password', models.CharField(max_length=128, verbose_name='Password')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_users', to='account.community')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]