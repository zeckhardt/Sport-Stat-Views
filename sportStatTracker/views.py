import matplotlib.pyplot as plt
import pandas as pd
from sportStatTracker import data
from django.shortcuts import render
import json

stat_names = {
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


def visualize_data(request):
    player_name = request.GET.get('player')
    stat = request.GET.get("stat")
    past = request.GET.get('range')
    season = '2023-24'

    player_stat = data.get_player_stat_data(player_name, stat, int(past), season)
    chart_data = {
        'labels': ['Game Dates', stat_names[stat], player_name, season, past],
        'dates': player_stat['GAME_DATE'].tolist(),
        'stat': player_stat[stat].tolist()
    }

    chart_data_json = json.dumps(chart_data)

    context = {
        'chart_data_json': chart_data_json
    }

    return render(request, 'visualization.html', context)


def input_data(request):
    return render(request, 'search.html')