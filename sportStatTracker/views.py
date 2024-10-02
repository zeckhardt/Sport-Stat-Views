import pandas as pd
from sportStatTracker import data
from django.shortcuts import render
import json

nba_player_stats = {
    'PTS': 'Points',
    'FG3M': 'Threes Made',
    'FG_PCT': 'Field Goal %',
    'FG3_PCT': 'Three Point %',
    'FT_PCT': 'Free Throw %',
    'REB': 'Rebounds',
    'AST': 'Assists',
    'STL': 'Steals',
    'BLK': 'Blocks',
    'TOV': 'Turnovers'
}

nfl_player_stats = {
    'pass_yds': 'Passing Yards',
    'pass_td': 'Passing Touchdowns',
    'rush_yds': 'Rushing Yards',
    'rush_td': 'Rushing Touchdowns',
    'int': 'Interceptions',
    'sacked': 'Sacks',
    'rec': 'Receptions',
    'rec_yds': 'Receiving Yards',
    'rec_td': 'Receiving Touchdowns',
    'tgt': 'Targets',
    'rush_att': 'Rush Attempts'
}


def nba_player_visualize(request):
    player_name = request.GET.get('player')
    stat = request.GET.get("stat")
    past = request.GET.get('range')
    season = '2023-24'

    player_stat = data.get_player_stat_data(player_name, stat, int(past), season)

    matchups = []
    for i in range(len(player_stat['MATCHUP'].tolist())):
        m = ' '.join(player_stat['MATCHUP'][i].split()[1:])
        matchups.append(m)

    chart_data = {
        'labels': ['Game Dates', nba_player_stats[stat], player_name, season, past],
        'WL': player_stat['WL'].tolist(),
        'matchups': matchups,
        'stat': player_stat[stat].tolist()
    }

    chart_data_json = json.dumps(chart_data)

    context = {
        'chart_data_json': chart_data_json
    }
    return render(request, 'playervisualization.html', context)


def nfl_player_visualize(request):
    player_name = request.GET.get('player')
    position = request.GET.get('position')
    stat = request.GET.get("stat")

    player_stat = data.get_nfl_stat_data(player_name, position, stat)
    matchups = []

    for i in range(len(player_stat['week'].tolist())):
        if player_stat['game_location'][i] == '@':
            game = f"Week {player_stat['week'][i]} @ {player_stat['opp'][i]}"
        else:
            game = f"Week {player_stat['week'][i]} vs {player_stat['opp'][i]}"

        matchups.append(game)

    chart_data = {
        'labels': ['Game Matchups', nfl_player_stats[stat], player_name, '2024'],
        'WL': player_stat['result'].tolist(),
        'matchups': matchups,
        'stat': player_stat[stat].tolist()
    }

    chart_data_json = json.dumps(chart_data)

    context = {
        'chart_data_json': chart_data_json
    }

    return render(request, 'playervisualization.html', context)


def input_nba_player(request):
    return render(request, 'nbaplayersearch.html')


def input_nfl_player(request):
    return render(request, 'nflplayersearch.html')


def home(request):
    return render(request, 'landing.html')