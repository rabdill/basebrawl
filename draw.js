function Display_Rumble(team1, team2) {
    data = alldata[team1][team2]

    display1 = document.getElementById('display1')
    idx = Math.floor(Math.random() * data[team1]['logs'].length)
    toprint = data[team1]['logs'][idx]
    console.log(toprint)
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
    element.innerHTML = `
        <h2>${name}: ${data[name]['wins']}&ndash;${data[opponent]['wins']}</h2>
        <button type="button" class="btn btn-primary" onclick="Display_Rumble('${name}','${opponent}')">Show random win log</button>
        <ul>
    `
    for (var fighter of Object.keys(data[name]['fighter_records'])) {
        element.innerHTML += `
            <li>${fighter}: ${data[name]['fighter_records'][fighter]['wins']}&ndash;${data[name]['fighter_records'][fighter]['losses']}
            </li>
        `
    }
}

function writeMatchups(teams) {
    console.log(teams)
    matchups1 = document.getElementById('matchups1')
    matchups2 = document.getElementById('matchups2')
    to_write1 = "<ul>"
    to_write2 = "<ul>"
    for(team1 of teams) {
        to_write1 += `<li><button type="button" class="btn btn-primary" onclick="SetTeam('${team1}', 1)">${team1}</button>`
        to_write2 += `<li><button type="button" class="btn btn-primary" onclick="SetTeam('${team1}', 2)">${team1}</button>`
    }
    to_write1 += "</ul>"
    to_write2 += "</ul>"
    matchups1.innerHTML=to_write1
    matchups2.innerHTML=to_write2
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

function SetTeam(team, num) {
    if(num == 1) {
        team1 = team
    } else {
        team2 = team
    }
    Display_Matchup()
}

team1 = 'Burps'
team2 = 'Farts'

console.log(alldata)
teams = Object.keys(alldata)
writeMatchups(teams)

team1 = teams[0]
team2 = teams[1]





// https://stackoverflow.com/questions/1265887/call-javascript-function-on-hyperlink-click