function Display_Rumble(team) {
    display1 = document.getElementById('display1')
    idx = Math.floor(Math.random() * data[team]['logs'].length)
    toprint = data[team]['logs'][idx]
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

function teamOverview(name, data, element) {
    teams = Object.keys(data)
    if(teams[0] == name) {
        opponent = teams[1]
    } else {
        opponent = teams[0]
    }
    element.innerHTML = `
        <h2>${name}: ${data[name]['wins']}&ndash;${data[opponent]['wins']}</h2>
        <button type="button" class="btn btn-primary" onclick="Display_Rumble('${name}')">Show random win log</button>
        <ul>
    `
    for (var fighter of Object.keys(data[name]['fighter_records'])) {
        element.innerHTML += `
            <li>${fighter}: ${data[name]['fighter_records'][fighter]['wins']}&ndash;${data[name]['fighter_records'][fighter]['losses']}
            </li>
        `
    }
}

a = document.getElementById('a')
b = document.getElementById('b')
console.log(data)
teams = Object.keys(data)
team1 = teams[0]
team2 = teams[1]
teamOverview(team1, data, a);
teamOverview(team2, data, b);




// https://stackoverflow.com/questions/1265887/call-javascript-function-on-hyperlink-click