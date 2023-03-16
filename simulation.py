from collections import defaultdict
import json

import fighting

def Fight(p1, p2, iterations):
    results = []
    for x in range(iterations):
        p1.reset()
        p2.reset()
        results.append(fighting.Fight(p1, p2, False))
    return(
        (results.count(1), results.count(2))
    )

def Rumble(t1, t2, iterations):
    records = []
    winners = []
    for x in range(iterations):
        for player in t1.fighters + t2.fighters:
            player.reset()

        z = fighting.Rumble(t1, t2)
        records.append(z)
        winners.append(z.winner)
    return((winners.count(t1.name), winners.count(t2.name), records))

def _record_fighter(fighter, to_record):
    """
    Convenience function that reads the results recorded by a single fighter,
    formats them the way we need for the Generate_report function, and returns
    the modified report for the next task.

    Input:
        - fighter: A Fighter object
        - to_record: A dictionary generated by Generate_report that will eventually
                be turned into JSON.

    Returns:
        - to_record: We update this dictionary and send it back
    """
    to_record[fighter.team]['fighter_records'][fighter.name] = {
        'wins': 0,
        'losses': 0,
        'matchups': defaultdict(lambda: [0,0]) # [wins, losses]
    }
    for opponent in fighter.wins:
        to_record[fighter.team]['fighter_records'][fighter.name]['matchups'][opponent][0] += 1
        to_record[fighter.team]['fighter_records'][fighter.name]['wins'] += 1
    for opponent in fighter.losses:
        to_record[fighter.team]['fighter_records'][fighter.name]['matchups'][opponent][1] += 1
        to_record[fighter.team]['fighter_records'][fighter.name]['losses'] += 1

    return(to_record)

def Generate_report(t1_wins, t2_wins, results, t1, t2):
    """
    Organizes results into a JSON document that can be loaded by an HTML
    dashboard.

    Input:
        - t1_wins: Integer. The number of team victories for team 1 (t1) in this matchup.
        - t2_wins: Integer. Same but for team 2
        - results: A list of RumbleReport objects for all simulated
            matchups between t1 and t2
        - t1: A Team object representing Team 1
        - t2: A Team object representing Team 2
    """
    to_record = {
        t1.name: {
            'wins': t1_wins,
            'logs': [],
            'fighter_records': {}
        },
        t2.name: {
            'wins': t2_wins,
            'logs': [],
            'fighter_records': {}
        }
    }
    #########
    # First, we load in the one-on-one fighter records
    #########
    # sort fighters by wins
    tosave = t1.fighters + t2.fighters
    tosave.sort(reverse=True, key=lambda x: len(x.wins))
    for fighter in tosave:
        to_record = _record_fighter(fighter, to_record)

    #########
    # Add logs to the winner's "logs" section
    #########
    for rumble in results:
        to_record[rumble.winner]['logs'].append([rumble.major_events, rumble.events])

    return(to_record)

def Record_reports(reports, players):
    """
    Input:
        reports - List of RumbleReport objects
        players - List of Fighter objects
    """
    #########
    # Write to file
    #########
    to_record = defaultdict(dict)
    known_teams = []
    for report in reports:
        teams = list(report.keys())
        to_record[teams[0]][teams[1]] = report
        to_record[teams[1]][teams[0]] = report
    with open("results.js", "w") as outfile:
        outfile.write('alldata=')
        json.dump(to_record, outfile)
    with open("players.js", "w") as outfile:
        player_record = {}
        for x in players:
            player_record[x.name] = x.print()
        outfile.write('\nplayers=')
        json.dump(player_record, outfile)
