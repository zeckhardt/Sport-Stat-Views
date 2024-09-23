from nba_api.stats.endpoints import playergamelog
from pro_football_reference_web_scraper import player_game_log as p
from nba_api.stats.static import players
import pandas as pd

pd.set_option("display.max_columns", None)


def get_player_id(player_name):
    player_dict = players.find_players_by_full_name(player_name)
    if player_dict:
        return player_dict[0]['id']
    return None


def get_player_game_log(player_id, season='2023-24'):
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    return game_log.get_data_frames()[0]


def get_player_stat_data(player_name: str, stat, range, season):
    game_log = get_player_game_log(get_player_id(player_name), season)
    print(game_log)

    if range == 0:
        return game_log[[stat, 'MATCHUP', 'WL']]

    return game_log.head(range)[[stat, 'MATCHUP', 'WL']]


def get_nfl_stat_data(player_name: str, position: str, stat):
    game_log = p.get_player_game_log(player=player_name, position=position, season=2024)

    return game_log[[stat, 'week', 'game_location', 'opp', 'result']]
