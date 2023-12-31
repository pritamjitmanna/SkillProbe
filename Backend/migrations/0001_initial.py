# Generated by Django 4.2.3 on 2023-09-15 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('challenge_id', models.AutoField(primary_key=True, serialize=False)),
                ('challenge_name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('challenge_time', models.IntegerField(default=0)),
                ('login_window', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Coding',
            fields=[
                ('problem_id', models.AutoField(primary_key=True, serialize=False)),
                ('problem_name', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('languages', models.JSONField(default=dict)),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coding', to='Backend.challenge')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=50, unique=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('contact', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('user_type', models.CharField(choices=[('company', 'Company'), ('candidate', 'Candidate')], max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('testcase_id', models.AutoField(primary_key=True, serialize=False)),
                ('testcase_name', models.CharField(max_length=100)),
                ('difficulty', models.CharField(choices=[('EASY', 'easy'), ('MEDIUM', 'medium'), ('HARD', 'hard')], max_length=6)),
                ('testcase', models.TextField()),
                ('output', models.TextField(default='')),
                ('is_sample', models.BooleanField(default=False)),
                ('problem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='testcase', to='Backend.coding')),
            ],
        ),
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('mcq_id', models.AutoField(primary_key=True, serialize=False)),
                ('q_name', models.CharField(max_length=100)),
                ('statement', models.TextField()),
                ('score', models.IntegerField()),
                ('q_options', models.JSONField(default=dict)),
                ('correctOptions', models.JSONField(default=dict)),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mcq', to='Backend.challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_uid', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge', to='Backend.company'),
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_uid', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('SocialMediaPlatforms', models.JSONField(default=dict)),
                ('education', models.JSONField(default=dict)),
                ('work_experience', models.JSONField(default=dict)),
                ('skills', models.JSONField(default=dict)),
                ('about', models.TextField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
