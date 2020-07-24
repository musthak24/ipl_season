import csv

from ipl.models import Match, Delivery


def csv_to_model1():
    file = 'matches.csv'
    with open(file) as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            match = Match()
            print(row[1])
            match.season = int(row[1])
            match.city = row[2]
            match.date = row[3]
            match.team1 = row[4]
            match.team2 = row[5]
            match.toss_winner = row[6]
            match.toss_decision = row[7]
            match.result = row[8]
            match.dl_applied = row[9]
            match.winner = row[10]
            match.win_by_run = row[11]
            match.win_by_wicket = row[12]
            match.player_of_match = row[13]
            match.venue = row[14]
            match.umpire1 = row[15]
            match.umpire2 = row[16]
            match.umpire3 = row[17]
            match.save()


def csv_to_model2():
    file = 'deliveries.csv'
    with open(file) as g:
        next(g)
        reader = csv.reader(g)
        for row in reader:
            delivery = Delivery(match_id=row[0])
            print(row[0])
            delivery.innings = int(row[1])
            delivery.batting_team = row[2]
            delivery.bowling_team = row[3]
            delivery.over = row[4]
            delivery.ball = row[5]
            delivery.batsman = row[6]
            delivery.non_striker = row[7]
            delivery.bowler = row[8]
            delivery.is_super_over = row[9]
            delivery.wide_run = row[10]
            delivery.bye_run = row[11]
            delivery.leg_bye_run = row[12]
            delivery.no_ball_run = row[13]
            delivery.penalty_run = row[14]
            delivery.batsmen_run = row[15]
            delivery.extra_run = row[16]
            delivery.total_run = row[17]
            delivery.player_dismissed = row[18]
            delivery.dismissal_kind = row[19]
            delivery.fielder = row[20]
            delivery.save()
