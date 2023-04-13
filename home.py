from nba_api.stats.endpoints import commonplayerinfo, LeagueLeaders, scoreboardv2, LeagueStandingsV3,commonallplayers, commonteamroster, playerfantasyprofile, shotchartdetail, shotchartlineupdetail, shotchartleaguewide, leaguedashoppptshot, leaguedashplayerptshot, leaguedashplayershotlocations, leaguedashteamptshot, leaguedashteamshotlocations, playerdashptshots, playerdashptshotdefend, TeamDashPtShots

import pandas, json, requests, os

teamIDs = [1610612743, 1610612749, 1610612738, 1610612763, 1610612758, 1610612755, 1610612739, 1610612746, 1610612752, 1610612756, 1610612744, 1610612748, 1610612750, 1610612751, 1610612737,
           1610612747, 1610612740, 1610612761, 1610612741, 1610612760, 1610612754, 1610612742, 1610612762, 1610612764, 1610612753, 1610612757, 1610612766, 1610612759, 1610612765, 1610612745]


# shotChartLP = shotchartlineupdetail.ShotChartLineupDetail(team_id_nullable=1610612740, context_measure_detailed="PTS")
# # print(shotChartLP.shot_chart_lineup_detail.get_data_frame())

# shotChartLeagueWide = shotchartleaguewide.ShotChartLeagueWide()
# # print(shotChartLeagueWide.get_data_frames())

# shotChartDetail = shotchartdetail.ShotChartDetail(team_id=1610612740, player_id=202685, opponent_team_id=1610612742)
# shotChartDetailMade = shotchartdetail.ShotChartDetail(team_id=1610612740, player_id=202685, season_nullable="2021-22")
# shotChartDetailAll = shotchartdetail.ShotChartDetail(team_id=1610612740, player_id=202685, context_measure_simple="FGA")

# chartLeagueAvgDF = shotChartDetailAll.league_averages.get_data_frame()
# chartMadeDF = shotChartDetailMade.shot_chart_detail.get_data_frame()
# chartAllDF = shotChartDetailAll.shot_chart_detail.get_data_frame()
# # print(chartLeagueAvgDF)
# # print(chartMadeDF)
# # print(chartAllDF)

# # chartAllDF.to_csv("shotChartDetail.csv", index=False)
# # chartLeagueAvgDF.to_csv("leagueShotChart.csv", index=False)

# teamDashPtsShots = TeamDashPtShots(team_id=1610612740, season="2022-23")
# teamDashPtsShotsDF = teamDashPtsShots.general_shooting.get_data_frame()
# teamDashPtsShotsClosestDF = teamDashPtsShots.closest_defender_shooting.get_data_frame()
# print(teamDashPtsShotsClosestDF)
# print(teamDashPtsShotsDF)
# teamDashPtsShotsDF.to_csv("pelicans_team_shots_general_shooting.csv", index=False)
# teamDashPtsShotsClosestDF.to_csv("pelicans_team_shots_closest.csv", index=False)

# leaguedashteamshotlocations = leaguedashteamshotlocations.LeagueDashTeamShotLocations(team_id_nullable= teamIDs[0], season="2022-23")

for teamID in teamIDs[0:30]:
    leaguedashteamshotlocation = leaguedashteamshotlocations.LeagueDashTeamShotLocations(team_id_nullable= teamID, season="2018-19")
    teamShotLocsDF = leaguedashteamshotlocation.shot_locations.get_data_frame()
    teamShotLocsDF.to_json(f'LeagueDashTeamShotLocations18-19/{teamID}.json')


# teamShotLocsDF = leaguedashteamshotlocations.shot_locations.get_data_frame()
# print(teamShotLocsDF)
# teamShotLocsDF.to_json('DenverShotLocs.json', orient='records')
# # teamShotLocsDF.to_csv("DenverShotLocs.csv", index=False)
# df = pandas.read_csv('DenverShotLocs.csv')
# print(type(df))