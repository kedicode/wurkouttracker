function hydrate_progression_exercises(event){
    select_exercise = (event.target.value);
    progression_select = document.getElementById("progression_exercises");
    current_progress_length = progression_select.options.length;
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
            for(let i = 0; i < exercises.length; i++){
                new_options.push(new Option(exercises[i]));
            }
            break;
        }
    case "one_arm_pullup":
        {
            break;
        }
    case "hanging_leg_raise":
        {
            break;
        }
    case "stand_to_stand_bridge":
        {
            break;
        }
    case "one_arm_handstand_pushups":
        {
            break;
        }
    case "one_leg_squat":
        {
            break;
        }
    default:
        {
            return;
        }

    }
    for(let i = 0; i < current_progress_length; i++){
        progression_select.remove(i);
    }
    for(let i = 0; i < exercises.length; i++){
        progression_select.add(new_options[i]);
    }

}


document.getElementById("master_exercises").addEventListener("change", hydrate_progression_exercises)
