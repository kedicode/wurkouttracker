from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

origins = ["*"]

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
    # TODO(Keenan) Finish the loading fo the master exercises
    #  "one-arm-pullup" : {
    #     "progressions" : {
    #         1 :  "Vertical Pullup",
    #         2 :  "Horizontal Pullup",
    #         3 :  "Jackknife Pullup",
    #         4 :  "Half Pullup",
    #         5 :  "Full Pullup",
    #         6 :  "Close",
    #         7 :  "Uneven Pullup",
    #         8 :  "1/2 One-Arm Pullup",
    #         9 :  "Assisted One-Arm Pullup",
    #         10 : "One-Arm Pullup"
    #     }
    # },
    # "one-arm-pullup" : {
    #     "progressions" : {
    #         1 :  "Vertical Pullup",
    #         2 :  "Horizontal Pullup",
    #         3 :  "Jackknife Pullup",
    #         4 :  "Half Pullup",
    #         5 :  "Full Pullup",
    #         6 :  "Close",
    #         7 :  "Uneven Pullup",
    #         8 :  "1/2 One-Arm Pullup",
    #         9 :  "Assisted One-Arm Pullup",
    #         10 : "One-Arm Pullup"
    #     }
    # },
    # "one-arm-pullup" : {
    #     "progressions" : {
    #         1 :  "Vertical Pullup",
    #         2 :  "Horizontal Pullup",
    #         3 :  "Jackknife Pullup",
    #         4 :  "Half Pullup",
    #         5 :  "Full Pullup",
    #         6 :  "Close",
    #         7 :  "Uneven Pullup",
    #         8 :  "1/2 One-Arm Pullup",
    #         9 :  "Assisted One-Arm Pullup",
    #         10 : "One-Arm Pullup"
    #     }
    # },
    # "one-arm-pullup" : {
    #     "progressions" : {
    #         1 :  "Vertical Pullup",
    #         2 :  "Horizontal Pullup",
    #         3 :  "Jackknife Pullup",
    #         4 :  "Half Pullup",
    #         5 :  "Full Pullup",
    #         6 :  "Close",
    #         7 :  "Uneven Pullup",
    #         8 :  "1/2 One-Arm Pullup",
    #         9 :  "Assisted One-Arm Pullup",
    #         10 : "One-Arm Pullup"
    #     }
    # }


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

@app.get("/workouts/{id}")
async def root(id: int):
    if id == 1:
        return "yay you got this working"
    return {"This would be some workouts"}
