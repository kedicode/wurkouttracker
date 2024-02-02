function clear_and_add_options(select_element, options_list){
    // options_length = select_element.options.length;
    // for(let i = 0; i < options_length; i++){
    //     select_element.remove(0);
    // }
    // for(let i = 0; i < options_list.length; i++){
    //     select_element.add(options_list[i]);
    // }
    select_element.replaceChildren();
    for(let i = 0; i < options_list.length; i++){
        select_element.add(options_list[i]);
    }
}

function hydrate_warmup(){
    // need to get the index of the selected progression exercise
    // build a new options list with the options that have ids <= the selected one
    warmup_options = [];
    progressions = document.getElementById("progression_exercises");
    progression_options = Array.from(progressions.options);
    selected_id = progressions.selectedIndex;
    for(let i = 0; i <= selected_id; i++){
        warmup_options.push(progression_options[i]);
    }
    console.log(progressions.options);
    console.log(warmup_options);
    warmup_select = document.getElementById("warmup_exercise");
    clear_and_add_options(warmup_select, warmup_options);
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
    clear_and_add_options(progression_select, new_options);
}

function show_hide_warmup(event){
    // we need to toggle so we need to get it
    warmup_toggle = document.getElementById("warmup_toggle");
    checked_value = event.target.checked;
    warmup_toggle.setAttribute(
        "style",
        checked_value ? "display: block" : "display: none");
    hydrate_warmup();
}


document.getElementById("master_exercises").addEventListener("change", hydrate_progression_exercises);

document.getElementById("has_warmup").addEventListener("change", show_hide_warmup);
