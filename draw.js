function Display_Rumble(team1, team2) {
    data = alldata[team1][team2]

    display1 = document.getElementById('display1')
    idx = Math.floor(Math.random() * data[team1]['logs'].length)
    toprint = data[team1]['logs'][idx]
    // Print major events
    display1.innerHTML = `
        <h3>Overview</h3>
        <ul>
    `
    for(entry of toprint[0]) {
        display1.innerHTML += `<li>${entry}</li>`
    }

    display1.innerHTML += `
        <h3>Play-by-play</h3>
    `
    for(entry of toprint[1]) {
        display1.innerHTML += `${entry}<br />`
    }
}

function teamOverview(name, opponent, data, element) {
    if(name == opponent) {
        // if the user selects a team to fight itself, just clear the window
        element.innerHTML = ''
        return
    }
    element.innerHTML = `
        <h2>${name}: ${data[name]['wins']}&ndash;${data[opponent]['wins']}</h2>
        <button type="button" class="btn btn-primary" onclick="Display_Rumble('${name}','${opponent}')">Show random win log</button>
        <ul>
    `
    for (var fighter of Object.keys(data[name]['fighter_records'])) {
        element.innerHTML += `
            <li>
            ${data[name]['fighter_records'][fighter]['fancyname']} <i class="bi-zoom-in" style="font-size: 1em;" data-bs-toggle="tooltip" data-bs-html="true" data-bs-title="${Player_Tip(fighter)}"></i>
            ${data[name]['fighter_records'][fighter]['wins']}&ndash;${data[name]['fighter_records'][fighter]['losses']}
            </li>
        `
    }
}

function Write_Team_Dropdowns(teams) {
    matchups1 = document.getElementById('matchups1')
    matchups2 = document.getElementById('matchups2')
    to_write1 = '<select class="form-select" id="team1" onchange="SetTeam(this, 1)">'
    to_write2 = '<select class="form-select" id="team2" onchange="SetTeam(this, 2)">'
    for(curteam of teams) {
        to_write1 += `<option value="${curteam}"`
        to_write2 += `<option value="${curteam}"`
        if(curteam == team1) {
            to_write1 += ` selected="selected"`
        } else if(curteam == team2) {
            to_write2 += ` selected="selected"`
        }
        to_write1 += `>${curteam}</option>`
        to_write2 += `>${curteam}</option>`
    }
    to_write1 += "</select>"
    to_write2 += "</select>"
    matchups1.innerHTML= to_write1
    matchups2.innerHTML= to_write2
}

function Display_Matchup() {
    a = document.getElementById('a')
    b = document.getElementById('b')
    teamOverview(team1, team2, alldata[team1][team2], a);
    teamOverview(team2, team1, alldata[team2][team1], b);

    // also clear whatever matchup was previously displayed
    display1 = document.getElementById('display1')
    display1.innerHTML = ''
}

function Player_Tip(player) {
    towrite = '<ul>'
    for (var trait of Object.keys(players[player]['fighter_stats'])) {
        towrite += `
            <li>${trait}: ${players[player]['fighter_stats'][trait]}</li>
        `
    }
    for (var tag of players[player]['tags']) {
        towrite += `<li>${tag.toUpperCase()}</li>`
    }
    towrite += "</ul>"
    return(towrite)
}

function SetTeam(selectbox, num) {
    if(typeof(selectbox) == 'string') {
        team = selectbox
    } else {
        team = selectbox.value // if it's from a dropdown
    }

    if(num == 1) {
        team1 = team
    } else {
        team2 = team
    }
    Display_Matchup()
}

team1 = 'South Jersey Schlemiels'
team2 = 'Daily Todays'

teams = Object.keys(alldata)
Write_Team_Dropdowns(teams)
SetTeam(team1, 1) // just print whatever the first matchup is

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
