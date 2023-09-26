# Generated by Django 4.2.5 on 2023-09-26 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField()),
                ('play_count', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('song', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='play.song')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='play.user')),
            ],
        ),
    ]
