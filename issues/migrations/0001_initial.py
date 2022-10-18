# Generated by Django 4.1.2 on 2022-10-14 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('summary', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.status')),
            ],
        ),
    ]
