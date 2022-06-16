
# Generated by Django 4.0.4 on 2022-06-16 08:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=225, unique=True, verbose_name='email')),
                ('first_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='last name')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)])),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator('^(09|\\+639)\\d{9}$', message='Phone number must begin with +639 or 09 followed by a 9 digits')])),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('SA', 'System Admin'), ('PH', 'Physician'), ('PA', 'Patient')], max_length=2, verbose_name='role')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=225, verbose_name='email')),
                ('first_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='last name')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)])),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator('^(09|\\+639)\\d{9}$', message='Phone number must begin with +639 or 09 followed by a 9 digits')])),
                ('role', models.CharField(choices=[('PH', 'Physician'), ('PA', 'Patient')], max_length=2, verbose_name='role')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('hospital_affiliation', models.CharField(blank=True, max_length=100, null=True)),
                ('account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=200)),
                ('room_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='prescriptions/')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='main.patient')),
                ('physician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='main.physician')),
            ],
        ),
        migrations.CreateModel(
            name='PatientConsultationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PCR', to='main.patient')),
                ('physician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.physician')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents/')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='main.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='main.patient')),
                ('physician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='main.physician')),
            ],
        ),
    ]
