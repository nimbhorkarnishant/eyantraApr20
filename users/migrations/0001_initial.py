# Generated by Django 3.0.5 on 2020-04-08 10:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_shopkeeper', models.BooleanField(verbose_name='Are you a shopkeeper')),
                ('shop_name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('dairy', 'dairy'), ('grocery', 'grocery'), ('electronics', 'electronics'), ('mechanic', 'mechanic')], max_length=30, null=True)),
                ('shop_address_line1', models.CharField(max_length=50)),
                ('shop_address_line2', models.CharField(blank=True, max_length=50)),
                ('shop_address_line3', models.CharField(blank=True, max_length=50)),
                ('shop_gmap_location', models.PositiveSmallIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)], verbose_name='Distance from center in km')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^[6-9]\\d{9}$')])),
                ('adhaar_no', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='eg. 1234 1234 1234', regex='^\\d{4}\\s\\d{4}\\s\\d{4}$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=50)),
                ('address_line2', models.CharField(blank=True, max_length=50)),
                ('address_line3', models.CharField(blank=True, max_length=50)),
                ('landmark', models.CharField(max_length=50)),
                ('additional_ph_no', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '[6-9]\\d{9}'. Up to 10 digits allowed.", regex='^[6-9]\\d{9}$')], verbose_name='additional_phone_number')),
                ('num_fam_mem', models.PositiveSmallIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], verbose_name='number_of_family_members')),
                ('gmap_location', models.PositiveSmallIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)], verbose_name='Distance from center in km')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
