from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
import pandas as pd
import matplotlib.pyplot as plt

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

    if range == 0:
        return game_log[[stat, 'GAME_DATE']]

    return game_log.head(range)[[stat, 'GAME_DATE']]
