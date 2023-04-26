from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

User = get_user_model()
BOOL_CHOICES = ((True, "True"), (False, "False"))


class configdata(models.Model):
    gameweek = models.PositiveIntegerField(default=0)
    season = models.PositiveIntegerField(default=2019)
    gw_deadline = models.DateTimeField(default=datetime.now)
    gw_active = models.BooleanField(default=False)
    gw_closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.gameweek} / {self.season}"

    class Meta:
        verbose_name = "Game Week Config"
        verbose_name_plural = "Game Week Config"


class Teams(models.Model):
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = "team"
        verbose_name_plural = "teams"


class Players(models.Model):
    player_name = models.CharField(max_length=100)
    player_team = models.ForeignKey(Teams, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_name

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"


class Question(models.Model):
    question_text = models.CharField(max_length=200, default="test")
    game_week = models.ForeignKey(
        configdata, models.CASCADE, related_name="Question_Game_Week"
    )
    TRUE = "TRUE"
    FALSE = "FALSE"
    question_choices = [(TRUE, "True"), (FALSE, "False")]
    question_answer = models.CharField(
        default=TRUE, choices=question_choices, max_length=5
    )

    def __str__(self):
        return self.question_text


class Fixtures(models.Model):
    home_team = models.ForeignKey(
        Teams, models.CASCADE, related_name="games_as_team1", null=True
    )
    away_team = models.ForeignKey(
        Teams, models.CASCADE, related_name="games_as_team2", null=True
    )
    game_week = models.ForeignKey(
        configdata, models.CASCADE, related_name="Fixture_Game_Week"
    )
    fix_weekid = models.PositiveIntegerField(default=0)
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)

    # start_time = models.DateTimeField()
    def __str__(self):
        return f"{self.home_team} v {self.away_team}"

    class Meta:
        verbose_name = "fixture"
        verbose_name_plural = "fixtures"


class entry_data_new(models.Model):
    entry_gw = models.ForeignKey(configdata, models.CASCADE, related_name="entry_GW")
    user_id = models.ForeignKey(User, models.CASCADE, related_name="entry_team")
    fixture_id1 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f1")
    score_home_fid1 = models.PositiveIntegerField(default=0)
    score_away_fid1 = models.PositiveIntegerField(default=0)
    fixture_id2 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f2")
    score_home_fid2 = models.PositiveIntegerField(default=0)
    score_away_fid2 = models.PositiveIntegerField(default=0)
    fixture_id3 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f3")
    score_home_fid3 = models.PositiveIntegerField(default=0)
    score_away_fid3 = models.PositiveIntegerField(default=0)
    fixture_id4 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f4")
    score_home_fid4 = models.PositiveIntegerField(default=0)
    score_away_fid4 = models.PositiveIntegerField(default=0)
    fixture_id5 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f5")
    score_home_fid5 = models.PositiveIntegerField(default=0)
    score_away_fid5 = models.PositiveIntegerField(default=0)
    fixture_id6 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f6")
    score_home_fid6 = models.PositiveIntegerField(default=0)
    score_away_fid6 = models.PositiveIntegerField(default=0)
    fixture_id7 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f7")
    score_home_fid7 = models.PositiveIntegerField(default=0)
    score_away_fid7 = models.PositiveIntegerField(default=0)
    fixture_id8 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f8")
    score_home_fid8 = models.PositiveIntegerField(default=0)
    score_away_fid8 = models.PositiveIntegerField(default=0)
    fixture_id9 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f9")
    score_home_fid9 = models.PositiveIntegerField(default=0)
    score_away_fid9 = models.PositiveIntegerField(default=0)
    fixture_id10 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f10")
    score_home_fid10 = models.PositiveIntegerField(default=0)
    score_away_fid10 = models.PositiveIntegerField(default=0)
    score_tg = models.PositiveIntegerField(default=0)
    scorer_player1_ff = models.CharField(max_length=50, null=True)
    scorer_player2_ff = models.CharField(max_length=50, null=True)
    scorer_player3_ff = models.CharField(max_length=50, null=True)
    scorer_player4_ff = models.CharField(max_length=50, null=True)
    TRUE = "TRUE"
    FALSE = "FALSE"
    question_choices = [(TRUE, "True"), (FALSE, "False")]
    question_id1 = models.ForeignKey(Question, models.CASCADE, related_name="qid_f1")
    question_answer_id1 = models.CharField(
        default=TRUE, choices=question_choices, max_length=5
    )
    question_id2 = models.ForeignKey(Question, models.CASCADE, related_name="qid_f2")
    question_answer_id2 = models.CharField(
        default=TRUE, choices=question_choices, max_length=5
    )
    question_id3 = models.ForeignKey(Question, models.CASCADE, related_name="qid_f3")
    question_answer_id3 = models.CharField(
        default=TRUE, choices=question_choices, max_length=5
    )
    question_id4 = models.ForeignKey(Question, models.CASCADE, related_name="qid_f4")
    question_answer_id4 = models.CharField(
        default=TRUE, choices=question_choices, max_length=5
    )
    question_id5 = models.ForeignKey(Question, models.CASCADE, related_name="qid_f5")
    question_answer_id5 = models.CharField(
        default=TRUE, choices=question_choices, max_length=5
    )
    question_id6 = models.ForeignKey(Question, models.CASCADE, related_name="qid_f6")
    question_answer_id6 = models.CharField(
        default=TRUE, choices=question_choices, max_length=5
    )
    question_id7 = models.ForeignKey(Question, models.CASCADE, related_name="qid_f7")
    question_answer_id7 = models.CharField(
        default=TRUE, choices=question_choices, max_length=5
    )
    question_id8 = models.ForeignKey(Question, models.CASCADE, related_name="qid_f8")
    question_answer_id8 = models.CharField(
        default=TRUE, choices=question_choices, max_length=5
    )
