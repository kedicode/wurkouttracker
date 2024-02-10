from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

class ExerciseLog(BaseModel):
    date:                    str
    master_exercises:        int
    progression_exercise:    int
    has_warmup:              bool | None = False
    warmup_exercise:         int
    warmup_set1:             int | None = None
    warmup_set2:             int | None = None
    main_set1:               int
    main_set2:               int
    main_set3:               int

origins = ["*"]

# TODO(Keenan) move this to a file as well.
master_exercises = {
    0 : {
        "name": "One-Arm Pullup",
        "progressions" : {
            0: "Vertical Pullup",
            1: "Horizontal Pullup",
            2: "Jackknife Pullup",
            3: "Half Pullup",
            4: "Full Pullup",
            5: "Close",
            6: "Uneven Pullup",
            7: "1/2 One-Arm Pullup",
            8: "Assisted One-Arm Pullup",
            9: "One-Arm Pullup"
        },
    },

    1 : {
        "name": "Hanging Leg Raise",
        "progressions" : {
            0: "Knee Tuck",
            1: "Knee Raise",
            2: "Bent Leg Raise",
            3: "Frog Leg Raise",
            4: "Flat Leg Raise",
            5: "Hanging Knee Raise",
            6: "Hanging Bent Leg Raise",
            7: "Hanging Frong Raise",
            8: "Partial Leg Raise",
            9: "Hanging Leg Raise"
        },
    },
    2 : {
        "name": "One Leg Squat",
        "progressions" : {
            0: "Shoulderstand Squat",
            1: "Jackknife Squat",
            2: "Supported Squat",
            3: "Half Squat",
            4: "Full Squat",
            5: "Close Squat",
            6: "Uneven Squat",
            7: "1/2 One-Leg Squat",
            8: "Assisted One-Leg Squat",
            9: "One-leg Squat"
        },

    },
    3 : {
        "name": "One Arm Pushup",
        "progressions" : {
            0: "Wall Pushup",
            1: "Incline Pushup",
            2: "Kneeling Pushup",
            3: "Half Pushup",
            4: "Full Pushup",
            5: "Close Pushup",
            6: "Uneven Pushup",
            7: "1/2 One-Arm Pushup",
            8: "Lever Pushup",
            9: "One-Arm Pushup"
        },
    },
    4 : {
        "name": "Stant to Stand Bridge",
        "progressions" : {
            0: "Short Bridge",
            1: "Straight Bridge",
            2: "Angled Bridge",
            3: "Head Bridge",
            4: "Half Bridge",
            5: "Full Bridge",
            6: "Wall Walking Bridges Down",
            7: "Wall Walking Bridges Up",
            8: "Closing Bridge",
            9: "Stant-to-Stand Bridge"
        },

    },
    5 : {
        "name": "One-Arm Handstand Pushup",
        "progressions" : {
            0: "Wall Headstand",
            1: "Crow Stand",
            2: "Wall Handstand",
            3: "Half Handstand Pushup",
            4: "Handstand Pushup",
            5: "Close Handstand Pushup",
            6: "Uneven Handstand Pushup",
            7: "1/2 One-Arm Handstand Pushup",
            8: "Lever Handstand Pushup",
            9: "One-Arm Handsta nd Pushup"
        },
    }
}

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

@app.get("/")
async def root():
    return master_exercises

@app.get("/workouts/")
async def workout_list():
    # TODO(Keenan) Lets see if we can add some date information
    # to the model that way we can then use it in the list of workouts
    # and essentially use a restfull route.
    workouts = []
    for dirs, path, files in os.walk("c:\\workout_logs"):
        for name in files:
            with open(os.path.join(dirs, name), 'r') as f:
                workouts.append(json.load(f))

    return workouts

@app.get("/workouts/{year}/{month}/{day}")
async def root(year: str, month: str, day: str):
    # query the files system for that year month day
    # combination and return the two logs that are
    # part of that comibination
    workouts = []
    path = os.path.join("c:\\workout_logs\\", year, month)
    for file in os.listdir(path):
        if file[0:2] == day:
            with open(os.path.join(path, file), 'r') as f:
                workouts.append(json.load(f))

    return workouts

@app.post("/add_workout/")
async def create_workout(exercise_log: ExerciseLog):
    exercise = master_exercises[exercise_log.master_exercises]
    # TODO(Keenan) add the ids in here so that this can be easily
    # parsed on the frontend
    log_entry = {
        "date": exercise_log.date,
        "master_exercise" : {
            "name": exercise["name"],
        },
        "progression_exercise": {
        "name": exercise["progressions"][exercise_log.progression_exercise],
            "level": exercise_log.progression_exercise + 1,
            "sets": [
                exercise_log.main_set1,
                exercise_log.main_set2,
                exercise_log.main_set3
            ]
        },
    }
    if exercise_log.has_warmup:
        log_entry["warmup_exercises"] = {
            "name": exercise["progressions"][exercise_log.warmup_exercise],
            "sets": [
                exercise_log.warmup_set1,
                exercise_log.warmup_set2
            ]
        }
    date_array = exercise_log.date.split('-')
    folder_date = f"{date_array[0]}\\{date_array[1]}"
    full_path = f"c:\\workout_logs\\{folder_date}"
    if not os.path.exists(full_path):
        os.makedirs(full_path, exist_ok = True)
    with open(f"c:\\workout_logs\\{folder_date}\\{date_array[2]}_{exercise['name']}.json", 'w') as f:
        json.dump(log_entry, f)
