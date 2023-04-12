from nba_api.stats.endpoints import commonplayerinfo, LeagueLeaders, scoreboardv2, LeagueStandingsV3,commonallplayers, commonteamroster, playerfantasyprofile, shotchartdetail, shotchartlineupdetail, shotchartleaguewide, leaguedashoppptshot, leaguedashplayerptshot, leaguedashplayershotlocations, leaguedashteamptshot, leaguedashteamshotlocations, playerdashptshots, playerdashptshotdefend, TeamDashPtShots

import pandas, json, requests, os

shotChartLP = shotchartlineupdetail.ShotChartLineupDetail(team_id_nullable=1610612740, context_measure_detailed="PTS")
print(shotChartLP.shot_chart_lineup_detail.get_data_frame())

shotChartLeagueWide = shotchartleaguewide.ShotChartLeagueWide()
print(shotChartLeagueWide.get_data_frames())

shotChartDetail = shotchartdetail.ShotChartDetail(team_id=1610612740, player_id=202685, opponent_team_id=1610612742)
shotChartDetailMade = shotchartdetail.ShotChartDetail(team_id=1610612740, player_id=202685, season_nullable="2021-22")
shotChartDetailAll = shotchartdetail.ShotChartDetail(team_id=1610612740, player_id=202685, context_measure_simple="FGA")

chartLeagueAvgDF = shotChartDetailAll.league_averages.get_data_frame()
chartMadeDF = shotChartDetailMade.shot_chart_detail.get_data_frame()
chartAllDF = shotChartDetailAll.shot_chart_detail.get_data_frame()
print(chartLeagueAvgDF)
# print(chartMadeDF)
# print(chartAllDF)

# chartAllDF.to_csv("shotChartDetail.csv", index=False)
chartLeagueAvgDF.to_csv("leagueShotChart.csv", index=False)