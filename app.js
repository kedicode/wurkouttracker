let exerciseData = {}


// TODO(Keenan) fix this as it won't work with api implementation
function hydrate_warmup(event){
    progress_index = event.target.selectedIndex;
    warmup_options = Array.from(event.target.options).slice(0, progress_index + 1);
    newOptions = [];
    for(let i = 0; i < warmup_options.length; i++){
        newOptions.push(new Option(warmup_options[i].text, warmup_options[i].value));
    }
    document.getElementById("warmup_exercise").replaceChildren(...newOptions);
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
    warmup_toggle = document.getElementById("warmup_toggle");
    checked_value = event.target.checked;
    // TODO(Keenan) make sure that these are removed on toggle
    set1Label = document.getElementById("warmup1Lbl");
    set2Label = document.getElementById("warmup2Lbl");
    input1 = document.createElement('input');
    input2 = document.createElement('input');
    input1.name = "warmup_set1";
    input1.type = "number";
    input1.min = 10;
    input1.max = 50;
    input2.name = "warmup_set2";
    input2.type = "number";
    input2.min = 10;
    input2.max = 50;
    set1Label.after(input1);
    set2Label.after(input2);
    warmup_toggle.setAttribute(
        "style",
        checked_value ? "display: block" : "display: none");
}

async function fetchExercises(){
    const response = await fetch("http://127.0.0.1:8000");
    exerciseData = await response.json();
}

document.getElementById("master_exercises").addEventListener("change", hydrate_progression_exercises);

document.getElementById("has_warmup").addEventListener("change", show_hide_warmup);

document.getElementById("progression_exercises").addEventListener("change", hydrate_warmup);

document.addEventListener("readystatechange", async () => {
    if(document.readyState === "complete"){
        console.log("in the event");
        await fetchExercises();
        loadMasterExercises();
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
    response = await fetch("http://127.0.0.1:8000/add_workout/",
                           {
                               method: "POST",
                               body: JSON.stringify(data),
                               headers: {
                                   "Content-Type": "application/json"
                               }
                           });
});
