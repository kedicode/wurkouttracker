function hydrate_warmup(event){
    progress_index = event.target.selectedIndex;
    warmup_options = Array.from(event.target.options).slice(0, progress_index + 1);
    newOptions = [];
    for(let i = 0; i < warmup_options.length; i++){
        newOptions.push(new Option(warmup_options[i].value));
    }
    document.getElementById("warmup_exercise").replaceChildren(...newOptions);
}

function hydrate_progression_exercises(event){
    select_exercise = (event.target.value);
    progression_select = document.getElementById("progression_exercises");
    new_options = [];
        switch(select_exercise){
    case "one_arm_pushup":
        {
            exercises = ['Wall Pushup',
                         'Incline Pushup',
                         'Kneeling Pushup',
                         'Half Pushup',
                         'Full Pushup',
                         'Close Pushup',
                         'Uneven Pushup',
                         '1/2 One-Arm Pushup',
                         'Lever Pushup',
                         'One-Arm Pushup'];
            break;
        }
    case "one_arm_pullup":
        {
            exercises = ['Vertical Pullup',
                         'Horizontal Pullup',
                         'Jackknife Pullup',
                         'Half Pullup',
                         'Full Pullup',
                         'Close Pullup',
                         'Uneven Pullup',
                         '1/2 One-Arm Pullup',
                         'Assisted One-Arm Pullup',
                         'One-Arm Pullup'];
            break;
        }
    case "hanging_leg_raise":
        {
            exercises = ['Knee Tuck',
                         'Knee Raise',
                         'Bent Leg Raise',
                         'Frog Leg Raise',
                         'Flat Leg Raise',
                         'Hanging Knee Raise',
                         'Hanging Bent Leg Raise',
                         'Hanging Frong Raise',
                         'Partial Leg Raise',
                         'Hanging Leg Raise'];
            break;
        }
    case "stand_to_stand_bridge":
        {
            exercises = ['Short Bridge',
                         'Straight Bridge',
                         'Angled Bridge',
                         'Head Bridge',
                         'Half Bridge',
                         'Full Bridge',
                         'Wall Walking Bridges Down',
                         'Wall Walking Bridges Up',
                         'Closing Bridge',
                         'Stant-to-Stand Bridge'];
            break;
        }
    case "one_arm_handstand_pushups":
        {
            exercises = ['Wall Headstand',
                         'Crow Stand',
                         'Wall Handstand',
                         'Half Handstand Pushup',
                         'Handstand Pushup',
                         'Close Handstand Pushup',
                         'Uneven Handstand Pushup',
                         '1/2 One-Arm Handstand Pushup',
                         'Lever Handstand Pushup',
                         'One-Arm Handstand Pushup'];
            break;
        }
    case "one_leg_squat":
        {
            exercises = ['Shoulderstand Squat',
                         'Jackknife Squat',
                         'Supported Squat',
                         'Half Squat',
                         'Full Squat',
                         'Close Squat',
                         'Uneven Squat',
                         '1/2 One-Leg Squat',
                         'Assisted One-Leg Squat',
                         'One-leg Squat'];
            break;
        }
    default:
        {
            return;
        }

    }
    for(let i = 0; i < exercises.length; i++){
        new_options.push(new Option(exercises[i]));
    }
    progression_select.replaceChildren(...new_options);
}

function show_hide_warmup(event){
    warmup_toggle = document.getElementById("warmup_toggle");
    checked_value = event.target.checked;
    warmup_toggle.setAttribute(
        "style",
        checked_value ? "display: block" : "display: none");
}


document.getElementById("master_exercises").addEventListener("change", hydrate_progression_exercises);

document.getElementById("has_warmup").addEventListener("change", show_hide_warmup);

document.getElementById("progression_exercises").addEventListener("change", hydrate_warmup);
