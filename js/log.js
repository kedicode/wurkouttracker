function hydrateLog(data){
    document.querySelector('h1').textContent = data[0].date;
    body = document.querySelector('#log_body');
    for (log of data){
        const tr = document.createElement('tr');
        const tdWarmup = document.createElement('td')
        const tdWarmupSet1 = document.createElement('td')
        const tdWarmupSet2 = document.createElement('td')
        tdWarmup.innerHTML = !log.warmup_exercises ? '&CircleTimes;' :
            log.warmup_exercises.name;
        if(!(!log.warmup_exercises)){
            tdWarmupSet1.textContent = log.warmup_exercises.sets[0];
            tdWarmupSet2.textContent =log.warmup_exercises.sets[1];
        }
        const tdMain = document.createElement('td')
        tdMain.textContent = log.progression_exercise.name
        const tdMain1 = document.createElement('td')
        tdMain1.textContent = log.progression_exercise.sets[0]
        const tdMain2 = document.createElement('td')
        tdMain2.textContent = log.progression_exercise.sets[1]
        const tdMain3 = document.createElement('td')
        tdMain3.textContent = log.progression_exercise.sets[2]
        tr.replaceChildren(tdWarmup, tdWarmupSet1, tdWarmupSet2, tdMain, tdMain1, tdMain2, tdMain3);
        body.appendChild(tr);
    }
}

document.addEventListener("readystatechange", async () => {
    if(document.readyState === "complete"){
        const dateParts = document.baseURI.split('?')[1].split('-')
        await fetch(`http://192.168.1.105:8000/workouts/${dateParts[0]}/${dateParts[1]}/${dateParts[2]}`)
            .then((response) => {
                return response.json();
            })
            .then(data => hydrateLog(data))
            .catch((error) => console.error("Error", error));
    }
});
