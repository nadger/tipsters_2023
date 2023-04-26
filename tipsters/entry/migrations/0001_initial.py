# Generated by Django 4.0.10 on 2023-04-11 15:04

import datetime
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
            name='configdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameweek', models.PositiveIntegerField(default=0)),
                ('season', models.PositiveIntegerField(default=2019)),
                ('gw_deadline', models.DateTimeField(default=datetime.datetime.now)),
                ('gw_active', models.BooleanField(default=False)),
                ('gw_closed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Game Week Config',
                'verbose_name_plural': 'Game Week Config',
            },
        ),
        migrations.CreateModel(
            name='Fixtures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fix_weekid', models.PositiveIntegerField(default=0)),
                ('home_score', models.IntegerField(blank=True, null=True)),
                ('away_score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'fixture',
                'verbose_name_plural': 'fixtures',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
            },
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_score', models.IntegerField()),
                ('away_score', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entry.fixtures')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='fixtures',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games_as_team2', to='entry.teams'),
        ),
        migrations.AddField(
            model_name='fixtures',
            name='game_week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fixture_Game_Week', to='entry.configdata'),
        ),
        migrations.AddField(
            model_name='fixtures',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games_as_team1', to='entry.teams'),
        ),
    ]
