from sportStatTracker import data
from django.shortcuts import render
import json

player_stat_mapping = {
    'nba': {
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
    },
    'nfl': {
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
}


def player_visualize(request, sport_type):
    player_name = request.GET.get('player')
    stat = request.GET.get("stat")
    past = request.GET.get('range')
    season = '2024-25' if sport_type == 'nba' else '2024'

    if sport_type == 'nba':
        player_stat = data.get_player_stat_data(player_name, stat, int(past), season)
        matchups = [m.split()[1:] for m in player_stat['MATCHUP']]
    else:  # NFL logic
        position = request.GET.get('position')
        player_stat = data.get_nfl_stat_data(player_name, position, stat)
        matchups = [
            f"Week {wk} {'@' if loc == '@' else 'vs'} {opp}"
            for wk, loc, opp in zip(player_stat['week'], player_stat['game_location'], player_stat['opp'])
        ]

    chart_data = {
        'labels': [
            'Game Dates' if sport_type == 'nba' else 'Game Matchups', player_stat_mapping[sport_type].get(stat, stat), player_name, season, past],
        'WL': player_stat['WL' if sport_type == 'nba' else 'result'].tolist() if sport_type == 'nfl' else player_stat['WL'][::-1],
        'matchups': matchups if sport_type == 'nfl' else matchups[::-1],
        'stat': player_stat[stat].tolist() if sport_type == 'nfl' else player_stat[stat].tolist()[::-1]
    }

    context = {'chart_data_json': json.dumps(chart_data)}
    return render(request, 'playervisualization.html', context)


def input_player(request, sport_type):
    template = 'nbaplayersearch.html' if sport_type == 'nba' else 'nflplayersearch.html'
    return render(request, template)


def home(request):
    return render(request, 'landing.html')