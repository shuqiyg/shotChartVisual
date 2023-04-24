# %%
import requests
import pandas as pd
from credentials import DEFAULT_HEADERS


def shotchartdetail(league_id='00', season='2019-20', season_type='Regular Season', team_id=0,
                    player_id=0, game_id='', outcome='', location='', month=0,
                    season_seg='', date_from='', date_to='', opp_team_id=0, vs_conf='',
                    vs_div='', pos='', game_seg='', per=0, last_n_games=0, ahead_behind='',
                    context_measure='FGM', clutch_time='', rookie_year=''):
    '''
    Access to NBA API - http://stats.nba.com/stats/shotchartdetail
    Returns the shotchart requested and the leagueaverage
    Example:
    shot_data,leagueaverage = shotchartdetail(season='2016-17')
    '''
    url = 'http://stats.nba.com/stats/shotchartdetail?'
    api_param = {
        'LeagueID': league_id,
        'Season': season,
        'SeasonType': season_type,
        'TeamID': team_id,
        'PlayerID': player_id,
        'GameID': game_id,
        'Outcome': outcome,
        'Location': location,
        'Month': month,
        'SeasonSegment': season_seg,
        'DateFrom': date_from,
        'DateTo': date_to,
        'OpponentTeamID': opp_team_id,
        'VsConference': vs_conf,
        'VsDivision': vs_div,
        'PlayerPosition': pos,
        'GameSegment': game_seg,
        'Period': per,
        'LastNGames': last_n_games,
        'AheadBehind': ahead_behind,
        'ContextMeasure': context_measure,
        'ClutchTime': clutch_time,
        'RookieYear': rookie_year,
    }
    response = requests.get(url, params=api_param, headers=DEFAULT_HEADERS)
    data = response.json()
    shot_chart_detail = pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])
    league_average = pd.DataFrame(data['resultSets'][1]['rowSet'], columns=data['resultSets'][1]['headers'])
    return shot_chart_detail, league_average
