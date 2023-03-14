import sys

import fighting
import models
import simulation

def load_saloon(rosterpath='rosters.csv'):
    batters = {}

    with open('batter_percentiles.csv', 'r', encoding='utf-8-sig') as infile:
        headers = infile.readline()[:-1].split(',')

        for line in infile:
            line = line[:-1].split(',')
            entry = {}
            for i in range(1, len(headers)): # skip player_name field
                try:
                    entry[headers[i]] = int(line[i])
                except ValueError:
                    entry[headers[i]] = None
            batters[line[0]] = entry
    with open(rosterpath,'r',encoding='utf-8-sig') as infile:
        team_names = []
        data = []
        for line in infile:
            player, team = line[:-1].split(',')
            if team not in team_names:
                team_names.append(team) # keep track of team names
            data.append((player,team))
    # once we've loaded all the rosters, we know the names of the teams and
    # can initialize them
    teams = {}
    for team_name in team_names:
        teams[team_name] = models.Team(team_name)
    # now we have Team objects for all the teams, and a way to address them.
    # next we create each player and add them to the team
    for entry in data:
        player_name, team_name = entry
        newb = models.Fighter(player_name)

        playerdata = batters.get(player_name)
        newb.convert_batter(playerdata)
        teams[team_name].add_fighter(newb)

    # Do the two-team rumble!
    to_record = []

    for team1 in team_names:
        for team2 in team_names:
            if team1 > team2:
                for player in teams[team1].fighters + teams[team2].fighters:
                    player.reset_all()
                results = simulation.Rumble(teams[team1], teams[team2], int(sys.argv[1]))
                print(f'\n{team1}: {results[0]}\n{team2}: {results[1]}')
                report = simulation.Generate_report(*results, teams[team1], teams[team2])
                to_record.append(report)
    simulation.Record_reports(to_record)

    # figure out how to get fighting stats from batting stats

    # repeat for pitching

    # (eventually, figure out how to save the data at this point so we can jump right back in
    # here, rather than loading every player and cross-referencing with rosters every time it runs.
    # but we don't have to do this until the stat conversions are actually set in stone.)

    # pit two teams against each other

    # once that's working ok, go back and add the one-on-one records so we can see if
    # some players always beat the same guys

    # then keep adding wrinkles to the fight calculations!

if __name__ == '__main__':
    #load_saloon('saloon.csv')
    load_saloon()