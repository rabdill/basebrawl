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
    matchups = document.getElementById('matchups')
    to_write = "<ul>"
    for(team1 in teams) {
        for(team2 in teams) {
            to_write += `<li><button type="button" class="btn btn-primary" onclick="Display_Matchup('"${team1}", "${team2}"')">${team1} vs ${team2}</button>`
        }
    }
    to_write += "</ul>"
    matchups.innerHTML=to_write
}

a = document.getElementById('a')
b = document.getElementById('b')

console.log(alldata)

teams = Object.keys(alldata)
writeMatchups(teams)

team1 = teams[0]
team2 = teams[1]
teamOverview(team1, team2, alldata[team1][team2], a);
teamOverview(team2, team1, alldata[team2][team1], b);




// https://stackoverflow.com/questions/1265887/call-javascript-function-on-hyperlink-click