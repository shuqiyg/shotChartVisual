from nba_api.stats.endpoints import commonplayerinfo, LeagueLeaders, scoreboardv2, LeagueStandingsV3,commonallplayers, commonteamroster, playerfantasyprofile, shotchartdetail, shotchartlineupdetail, shotchartleaguewide, leaguedashoppptshot, leaguedashplayerptshot, leaguedashplayershotlocations, leaguedashteamptshot, leaguedashteamshotlocations, playerdashptshots, playerdashptshotdefend, TeamDashPtShots, PlayerEstimatedMetrics

import pandas, json, requests, os, time, plotly.express as px

player_estimated_metrics = PlayerEstimatedMetrics(season="2022-23", season_type="Regular Season").player_estimated_metrics.get_data_frame()
df = player_estimated_metrics.loc[(player_estimated_metrics['GP'] >= 50) & (
    player_estimated_metrics['MIN'] >= 20)]
# df.to_csv("off_def_rating.csv", index=False)
df = df.sort_values(by="E_DEF_RATING", ascending=False)
print(df[['PLAYER_NAME','GP','MIN','E_DEF_RATING']])

fig = px.scatter(df, x='E_OFF_RATING', y='E_DEF_RATING', hover_name='PLAYER_NAME')
fig.update_layout(yaxis=dict(autorange="reversed"))
fig.show()


teamIDs = [1610612743, 1610612749, 1610612738, 1610612763, 1610612758, 1610612755, 1610612739, 1610612746, 1610612752, 1610612756, 1610612744, 1610612748, 1610612750, 1610612751, 1610612737,
           1610612747, 1610612740, 1610612761, 1610612741, 1610612760, 1610612754, 1610612742, 1610612762, 1610612764, 1610612753, 1610612757, 1610612766, 1610612759, 1610612765, 1610612745]

# fetch LeagueDashTeamShotLocations 2018-19 - 2022-23
# for teamID in teamIDs[0:30]:
#     leaguedashteamshotlocation = leaguedashteamshotlocations.LeagueDashTeamShotLocations(team_id_nullable= teamID, season="2018-19")
#     teamShotLocsDF = leaguedashteamshotlocation.shot_locations.get_data_frame()
#     teamShotLocsDF.to_json(f'LeagueDashTeamShotLocations18-19/{teamID}.json')

# create a json file for teamID and RosterIDs pairs
# teamRosterIdsPairs = {}
# for teamID in teamIDs[0:10]:
#     ctr = commonteamroster.CommonTeamRoster(team_id=teamID, season="2018-19")
#     ctrDF = ctr.common_team_roster.get_data_frame()
#     crtArray = ctrDF["PLAYER_ID"].to_numpy()
#     print(crtArray)
#     teamRosterIdsPairs[teamID] = crtArray.tolist()
# time.sleep(5)
# for teamID in teamIDs[10:20]:
#     ctr = commonteamroster.CommonTeamRoster(team_id=teamID,season="2018-19")
#     ctrDF = ctr.common_team_roster.get_data_frame()
#     crtArray = ctrDF["PLAYER_ID"].to_numpy()
#     print(crtArray)
#     teamRosterIdsPairs[teamID] = crtArray.tolist()
# time.sleep(5)
# for teamID in teamIDs[20:30]:
#     ctr = commonteamroster.CommonTeamRoster(team_id=teamID, season="2018-19")
#     ctrDF = ctr.common_team_roster.get_data_frame()
#     crtArray = ctrDF["PLAYER_ID"].to_numpy()
#     print(crtArray)
#     teamRosterIdsPairs[teamID] = crtArray.tolist()
# with open("teamRosterIdsPairs18-19.json", "a") as jFile:
#     json.dump(teamRosterIdsPairs, jFile)

#fetch shotchartdetail of every single player for the regular seasons
# with open("teamRosterIdsPairs18-19.json", "r") as trpJson:
#     data = json.load(trpJson)
# print(type(data))
# print(data)
# size = 0
# for teamID in teamIDs:
#     for playerID in data[str(teamID)]:
#         size+=1

# print(size)
# idsArray = data[str(teamIDs[3])]
# print(idsArray)
# print(teamIDs[0])

# for teamID in teamIDs[3:30]:
#     for id in data[str(teamID)]:
#         shotChartDetailAll = shotchartdetail.ShotChartDetail(
#             season_nullable="2018-19", team_id=teamID, player_id=id, context_measure_simple="FGA")
#         shotChartDetailAllDF = shotChartDetailAll.shot_chart_detail.get_data_frame();
#         print(shotChartDetailAllDF)
#         # with open(f"shotChartDetail/{teamIDs[0]}/{id}.json", "a") as jFile:
#         #     json.dump(shotChartDetailAllDF.to_json(), jFile)
#         shotChartDetailAllDF.to_json(f'shotChartDetail18-19/{teamID}/{id}.json')
#     time.sleep(6)



# shotChartLP = shotchartlineupdetail.ShotChartLineupDetail(season_type_all_star='Regular Season', season='2021-22', context_measure_detailed='FGA', period=0, team_id_nullable=0,game_id_nullable=0)
# print(shotChartLP.shot_chart_lineup_detail.get_data_frame())

# shotChartLeagueWide = shotchartleaguewide.ShotChartLeagueWide()
# # print(shotChartLeagueWide.get_data_frames())

# shotChartDetail = shotchartdetail.ShotChartDetail(team_id=1610612740, player_id=202685, opponent_team_id=1610612742)
# shotChartDetailMade = shotchartdetail.ShotChartDetail(team_id=1610612740, player_id=202685, season_nullable="2021-22")
# shotChartDetailAll = shotchartdetail.ShotChartDetail(team_id=1610612740, player_id=202685, context_measure_simple="FGA")
# for teamID in teamIDs[0:5]:
#     leaguedashteamshotlocation = leaguedashteamshotlocations.LeagueDashTeamShotLocations(team_id_nullable= teamID, season="2018-19")
#     teamShotLocsDF = leaguedashteamshotlocation.shot_locations.get_data_frame()
#     teamShotLocsDF.to_json(f'LeagueDashTeamShotLocations18-19/{teamID}.json')

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




# teamShotLocsDF = leaguedashteamshotlocations.shot_locations.get_data_frame()
# print(teamShotLocsDF)
# teamShotLocsDF.to_json('DenverShotLocs.json', orient='records')
# # teamShotLocsDF.to_csv("DenverShotLocs.csv", index=False)
# df = pandas.read_csv('DenverShotLocs.csv')
# print(type(df))