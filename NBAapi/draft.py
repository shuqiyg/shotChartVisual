import requests
import pandas as pd
from NBAapi.credentials import DEFAULT_HEADERS

def drafthistory(college='', leagueid='00', overallpick='', roundnum='', roundpick='',
                 season='', teamid=0, topx=''):
    url = 'https://stats.nba.com/stats/drafthistory?'
    api_param = {
        'College': college,
        'LeagueID': leagueid,
        'OverallPick': overallpick,
        'RoundNum': roundnum,
        'RoundPick': roundpick,
        'Season': season,
        'TeamID': teamid,
        'TopX': topx
    }
    response = requests.get(url, params=api_param,
                            headers=DEFAULT_HEADERS)
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])
