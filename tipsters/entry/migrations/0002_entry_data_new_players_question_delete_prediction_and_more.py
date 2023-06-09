# Generated by Django 4.0.10 on 2023-04-19 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='entry_data_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_home_fid1', models.PositiveIntegerField(default=0)),
                ('score_away_fid1', models.PositiveIntegerField(default=0)),
                ('score_home_fid2', models.PositiveIntegerField(default=0)),
                ('score_away_fid2', models.PositiveIntegerField(default=0)),
                ('score_home_fid3', models.PositiveIntegerField(default=0)),
                ('score_away_fid3', models.PositiveIntegerField(default=0)),
                ('score_home_fid4', models.PositiveIntegerField(default=0)),
                ('score_away_fid4', models.PositiveIntegerField(default=0)),
                ('score_home_fid5', models.PositiveIntegerField(default=0)),
                ('score_away_fid5', models.PositiveIntegerField(default=0)),
                ('score_home_fid6', models.PositiveIntegerField(default=0)),
                ('score_away_fid6', models.PositiveIntegerField(default=0)),
                ('score_home_fid7', models.PositiveIntegerField(default=0)),
                ('score_away_fid7', models.PositiveIntegerField(default=0)),
                ('score_home_fid8', models.PositiveIntegerField(default=0)),
                ('score_away_fid8', models.PositiveIntegerField(default=0)),
                ('score_home_fid9', models.PositiveIntegerField(default=0)),
                ('score_away_fid9', models.PositiveIntegerField(default=0)),
                ('score_home_fid10', models.PositiveIntegerField(default=0)),
                ('score_away_fid10', models.PositiveIntegerField(default=0)),
                ('score_tg', models.PositiveIntegerField(default=0)),
                ('scorer_player1_ff', models.CharField(max_length=50, null=True)),
                ('scorer_player2_ff', models.CharField(max_length=50, null=True)),
                ('scorer_player3_ff', models.CharField(max_length=50, null=True)),
                ('scorer_player4_ff', models.CharField(max_length=50, null=True)),
                ('question_answer_id1', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='TRUE', max_length=5)),
                ('question_answer_id2', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='TRUE', max_length=5)),
                ('question_answer_id3', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='TRUE', max_length=5)),
                ('question_answer_id4', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='TRUE', max_length=5)),
                ('question_answer_id5', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='TRUE', max_length=5)),
                ('question_answer_id6', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='TRUE', max_length=5)),
                ('question_answer_id7', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='TRUE', max_length=5)),
                ('question_answer_id8', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='TRUE', max_length=5)),
                ('entry_gw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_GW', to='entry.configdata')),
                ('fixture_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f1', to='entry.fixtures')),
                ('fixture_id10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f10', to='entry.fixtures')),
                ('fixture_id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f2', to='entry.fixtures')),
                ('fixture_id3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f3', to='entry.fixtures')),
                ('fixture_id4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f4', to='entry.fixtures')),
                ('fixture_id5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f5', to='entry.fixtures')),
                ('fixture_id6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f6', to='entry.fixtures')),
                ('fixture_id7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f7', to='entry.fixtures')),
                ('fixture_id8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f8', to='entry.fixtures')),
                ('fixture_id9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fid_f9', to='entry.fixtures')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('player_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entry.teams')),
            ],
            options={
                'verbose_name': 'player',
                'verbose_name_plural': 'players',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default='test', max_length=200)),
                ('question_answer', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='TRUE', max_length=5)),
                ('game_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Question_Game_Week', to='entry.configdata')),
            ],
        ),
        migrations.DeleteModel(
            name='Prediction',
        ),
        migrations.AddField(
            model_name='entry_data_new',
            name='question_id1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qid_f1', to='entry.question'),
        ),
        migrations.AddField(
            model_name='entry_data_new',
            name='question_id2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qid_f2', to='entry.question'),
        ),
        migrations.AddField(
            model_name='entry_data_new',
            name='question_id3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qid_f3', to='entry.question'),
        ),
        migrations.AddField(
            model_name='entry_data_new',
            name='question_id4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qid_f4', to='entry.question'),
        ),
        migrations.AddField(
            model_name='entry_data_new',
            name='question_id5',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qid_f5', to='entry.question'),
        ),
        migrations.AddField(
            model_name='entry_data_new',
            name='question_id6',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qid_f6', to='entry.question'),
        ),
        migrations.AddField(
            model_name='entry_data_new',
            name='question_id7',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qid_f7', to='entry.question'),
        ),
        migrations.AddField(
            model_name='entry_data_new',
            name='question_id8',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qid_f8', to='entry.question'),
        ),
        migrations.AddField(
            model_name='entry_data_new',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_team', to=settings.AUTH_USER_MODEL),
        ),
    ]
