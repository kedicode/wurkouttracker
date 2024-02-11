let exerciseData = {}


function hydrate_warmup(event){
    progress_index = event.target.selectedIndex;
    warmup_options = Array.from(event.target.options).slice(0, progress_index + 1);
    newOptions = [];
    for(let i = 0; i < warmup_options.length; i++){
        newOptions.push(new Option(warmup_options[i].text, warmup_options[i].value));
    }
    document.getElementById("warmup_exercise").replaceChildren(...newOptions);
}

function hydrateWorkoutTable(data){
    table = document.querySelector('#workout_table');
    table.replaceChildren('');
    for(log of data){
        tr = document.createElement('tr');
        dateTd = document.createElement('td');
        dateA = document.createElement('a');
        dateA.href = `log.html?${log.date}`;
        masterTd = document.createElement('td');
        progressTd = document.createElement('td');
        levelTd = document.createElement('td');
        hasWarmupTd = document.createElement('td');
        dateA.textContent = log.date;
        dateTd.appendChild(dateA)
        masterTd.textContent = log.master_exercise.name;
        progressTd.textContent = log.progression_exercise.name;
        levelTd.textContent = log.progression_exercise.level;
        hasWarmupTd.innerHTML = !log.warmup_exercises ? '&CircleTimes;' : '&check;';
        tr.replaceChildren(dateTd, masterTd, progressTd, levelTd, hasWarmupTd);
        table.appendChild(tr);
    }
}

async function loadMasterExercises(exercises){
    newOptions = [];
    newOptions.push(new Option("--Select and Option--"))
    for(ex in exerciseData){
        console.log(ex);
        curr_item = exerciseData[ex];
        newOptions.push(new Option(curr_item['name'], ex));
    }
    document.getElementById("master_exercises").replaceChildren(...newOptions);
}

function hydrate_progression_exercises(event){
    select_exercise = parseInt(event.target.value);
    progression_select = document.getElementById("progression_exercises");
    new_options = [];
    exercises = exerciseData[select_exercise]['progressions'];
    for(ex in exercises){
        curr_item = exercises[ex];
        new_options.push(new Option(curr_item, ex));
    }
    progression_select.replaceChildren(...new_options);
}

function show_hide_warmup(event){
    document.querySelectorAll(".warmup_input").forEach(e => e.remove());
    warmup_toggle = document.getElementById("warmup_toggle");
    checked_value = event.target.checked;
    set1Label = document.getElementById("warmup1Lbl");
    set2Label = document.getElementById("warmup2Lbl");
    if(checked_value) {
        input1 = document.createElement('input');
        input1.classList.add('warmup_input', 'input')
        input2 = document.createElement('input');
        input2.classList.add('warmup_input', 'input')
        input1.name = "warmup_set1";
        input1.type = "number";
        input1.min = 10;
        input1.max = 50;
        input2.name = "warmup_set2";
        input2.type = "number";
        input2.min = 10;
        input2.max = 50;
        input1.value = 0;
        input2.value = 0;
        set1Label.after(input1);
        set2Label.after(input2);
    }
    warmup_toggle.setAttribute(
        "style",
        checked_value ? "display: block" : "display: none");
}

async function fetchExercises(){
    try {
        const response = await fetch("http://192.168.1.105:8000");
        exerciseData = await response.json();
    }
    catch(error){
        alert(error);
    }
}

async function fetchLogs(){
    const response = await fetch("http://192.168.1.105:8000/workouts/");
    return await response.json();
}

document.getElementById("master_exercises").addEventListener("change", hydrate_progression_exercises);

document.getElementById("has_warmup").addEventListener("change", show_hide_warmup);

document.getElementById("progression_exercises").addEventListener("change", hydrate_warmup);

document.addEventListener("readystatechange", async () => {
    if(document.readyState === "complete"){
        console.log("in the event");
        await fetchExercises();
        loadMasterExercises();
        const logData = await fetchLogs();
        hydrateWorkoutTable(logData);
    }
});

document.addEventListener("submit", async (event) => {
    event.preventDefault();
    formElm = document.getElementById("workout_form");
    const formData = new FormData(formElm);
    const data = {};
    for(let [key, value] of formData.entries()){
        data[key] = value;
    }
    try {
        response = await fetch("http://192.168.1.105:8000/add_workout/",
                               {
                                   method: "POST",
                                   body: JSON.stringify(data),
                                   headers: {
                                       "Content-Type": "application/json"
                                   }
                               });
        if(response.status === 200){
            const logs = await fetchLogs();
            hydrateWorkoutTable(logs);
        }
    }
    catch(error) {
        console.error("Error", error);
    }
});
