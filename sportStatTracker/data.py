import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from pro_football_reference_web_scraper import player_game_log as p

pd.set_option("display.max_columns", None)


def get_player_id(player_name):
    """
    Find the NBA player ID for a given full name.

    Args:
        player_name (str): The full name of the NBA player.

    Returns:
        str: The NBA player ID if found, None otherwise.
    """
    player_dict = players.find_players_by_full_name(player_name)
    if player_dict:
        return player_dict[0]['id']
    return None


def get_player_game_log(player_id, season='2023-24'):
    """
    Retrieve the player's game log data for a specified season.

    Args:
        player_id (str): The NBA player ID.
        season (str, optional): The NBA season in the format 'YYYY-YY'. Defaults to '2023-24'.

    Returns:
        pandas.DataFrame: The player's game log data.
    """
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    return game_log.get_data_frames()[0]


def get_player_stat_data(player_name, stat, range=0, season='2023-24'):
    """
    Retrieve specific player statistics from their game log.

    Args:
        player_name (str): The full name of the NBA player.
        stat (str): The name of the statistic to retrieve.
        range (int, optional): The number of games to retrieve. 0 for all games. Defaults to 0.
        season (str, optional): The NBA season in the format 'YYYY-YY'. Defaults to '2023-24'.

    Returns:
        pandas.DataFrame: A DataFrame containing the specified statistic, matchup, and W/L result.
    """
    player_id = get_player_id(player_name)
    game_log = get_player_game_log(player_id, season)

    required_columns = [stat, 'MATCHUP', 'WL']
    data = game_log[required_columns]

    if range > 0:
        data = data.head(range)

    return data


def get_nfl_stat_data(player_name, position, stat):
    """
    Retrieve specific NFL statistic data for a player and position.

    Args:
        player_name (str): The full name of the NFL player.
        position (str): The player's position.
        stat (str): The name of the statistic to retrieve.

    Returns:
        pandas.DataFrame: A DataFrame containing the specified statistic, week, game details, and result.
    """
    game_log = p.get_player_game_log(player=player_name, position=position, season=2024)
    required_columns = [stat, 'week', 'game_location', 'opp', 'result']
    return game_log[required_columns]