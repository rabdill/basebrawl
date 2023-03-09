function teamOverview(name, data, element) {
    teams = Object.keys(data)
    if(teams[0] == name) {
        opponent = teams[1]
    } else {
        opponent = teams[0]
    }
    element.innerHTML = `
        <h2>${name}: ${data[name]['wins']}&ndash;${data[opponent]['wins']}</h2>
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

teamOverview(teams[0], data, a);
teamOverview(teams[1], data, b);
