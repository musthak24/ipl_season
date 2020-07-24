from django.db import models


# Create your models here.
class Match(models.Model):
    season = models.IntegerField()
    city = models.CharField(max_length=255)
    date = models.DateField()
    team1 = models.CharField(max_length=255)
    team2 = models.CharField(max_length=255)
    toss_winner = models.CharField(max_length=255)
    toss_decision = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    dl_applied = models.BooleanField(default=False)
    winner = models.CharField(max_length=255)
    win_by_run = models.IntegerField()
    win_by_wicket = models.IntegerField()
    player_of_match = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    umpire1 = models.CharField(max_length=255, null=True)
    umpire2 = models.CharField(max_length=255, null=True)
    umpire3 = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)


class Delivery(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    innings = models.IntegerField()
    batting_team = models.CharField(max_length=255)
    bowling_team = models.CharField(max_length=255)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=255)
    non_striker = models.CharField(max_length=255)
    bowler = models.CharField(max_length=255)
    is_super_over = models.BooleanField(default=False)
    wide_run = models.IntegerField()
    bye_run = models.IntegerField()
    leg_bye_run = models.IntegerField()
    no_ball_run = models.IntegerField()
    penalty_run = models.IntegerField()
    batsmen_run = models.IntegerField()
    extra_run = models.IntegerField()
    total_run = models.IntegerField()
    player_dismissed = models.CharField(max_length=255,null=True)
    dismissal_kind = models.CharField(max_length=255,null=True)
    fielder = models.CharField(max_length=255,null=True)
