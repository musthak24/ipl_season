from django.contrib.auth.decorators import login_required
from django.db.models import Max, Count
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from ipl.form import SeasonForm
from ipl.models import Match, Delivery


#
# function for getting top teams of the season
#
def get_top_team(match, season):
    return match.filter(winner__isnull=False, season=season).values_list('winner', flat=True).annotate(
        dcount=Count('winner')).order_by('-dcount')[:4]


#
# function for getting most number of toss winner of the season
#
def get_tos_winner(match, season):
    return match.filter(season=season).values_list('toss_winner', flat=True).annotate(
        dcount=Count('toss_winner')).order_by('-dcount')[0]


#
# function for getting max number of player award of the season
#
def get_max_player_award(match, season):
    return match.filter(season=season).values_list('player_of_match', flat=True).annotate(
        dcount=Count('player_of_match')).order_by('-dcount')[0]


#
# function for getting max number of win location for the top team of the season
#
def ge_location_win_more(match, season, winner):
    return match.filter(season=season, winner=winner).values_list('city', flat=True).annotate(
        dcount=Count('city')).order_by('-dcount')[0]


#
# function for getting  toss percentage of the teams who won the toss and chose to bat
#
def win_percentage_toss(match, season):
    match = match.filter(season=season)
    count = match.count()
    bat = match.filter(toss_decision='bat').count()
    percentage = bat * 100 / count
    if percentage:
        percentage = percentage
        percentage = round(percentage, 2)

    list1 = match.filter(season=season, toss_decision='bat').values_list('toss_winner').annotate(
        dcount=Count('toss_winner')).order_by('-dcount')
    list2 = match.filter(season=season, toss_decision='field').values_list('toss_winner').annotate(
        dcount=Count('toss_winner')).order_by('-dcount')
    list1 = list(list1)
    list2 = list(list2)

    data = {}
    for l1 in list1:
        for l2 in list2:
            if l1[0] == l2[0]:
                calc = round(l1[1] / (l1[1] + l2[1]) * 100, 2)
                data[l1[0]] = calc
        if l1[0] not in data:
            data[l1[0]] = 100
    return percentage, data


#
# function for getting location  hosted most number of matches of the season
#
def location_most_matches(match, season):
    return match.filter(season=season).values_list('city').annotate(
        dcount=Count('city')).order_by('-dcount')[0]


#
# function for getting team won by the highest margin of runs  of the season
#

def high_margin_win_run(match, season):
    return match.filter(season=season).values('winner').annotate(run=Max('win_by_run')).order_by('-run')[0]


#
# function for getting team won by the highest margin of wickets  for the season
#

def high_margin_win_wicket(match, season):
    return match.filter(season=season).values('winner').annotate(run=Max('win_by_wicket')).order_by('-run')[0]


#
# function for getting team won toss and match for the season
#

def won_toss_and_match(match, season):
    my_dict = {}
    obj = match.filter(season=season).values_list('toss_winner', 'winner')
    for i in obj:
        count = 1
        if i[0] == i[1]:
            if i[0] in my_dict:
                my_dict[i[0]] = my_dict[i[0]] + 1
            else:
                my_dict[i[0]] = count
    return my_dict


#
# Most number of catches by a fielder in a match for the season
#

def most_number_catches(season):
    catches = Delivery.objects.filter(match__season=season, dismissal_kind='caught').values_list('match_id',
                                                                                                 'fielder').annotate(
        dcount=Count('fielder')).order_by('-dcount')
    if catches:
        catches = catches[0]
    return catches


@method_decorator(login_required, name='dispatch')
class Home(View):
    def get(self, request):
        form = SeasonForm
        return render(request, 'home.html', {'form': form})

    def post(self, request):
        form = SeasonForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('season')
            print('data', data)
            return redirect('season_detail', pk=data)
        return render(request, 'home.html', {'form': form})


@login_required
def get_details(request, pk):
    season = pk

    match = Match.objects.all()
    winner = get_top_team(match, season)
    tos_winner = get_tos_winner(match, season)
    player_of_match = get_max_player_award(match, season)

    location = ge_location_win_more(match, season, winner[0])
    percentage, percent_details = win_percentage_toss(match, season)
    most_matches = location_most_matches(match, season)

    high_margin_run = high_margin_win_run(match, season)
    high_margin_run = list(high_margin_run.items())

    high_margin_wicket = high_margin_win_wicket(match, season)
    high_margin_wicket = list(high_margin_wicket.items())

    won_tos_match = won_toss_and_match(match, season)
    most_catches = most_number_catches(season)
    return render(request, 'season_detail.html', {'season': season,
                                                  'winner': winner,
                                                  'tos_winner': tos_winner,
                                                  'player_award': player_of_match,
                                                  'topper': winner[0],
                                                  'location': location,
                                                  'percentage': percentage,
                                                  'most_matches': most_matches,
                                                  'high_margin_run': high_margin_run,
                                                  'high_margin_wicket': high_margin_wicket,
                                                  'won_toss_match': won_tos_match,
                                                  'most_catches': most_catches,
                                                  'percent_details': percent_details})
