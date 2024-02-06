from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

origins = ["*"]

master_exercises = {
    "one_arm_pullup" : {
        "progressions" : {
            1 :  "Vertical Pullup",
            2 :  "Horizontal Pullup",
            3 :  "Jackknife Pullup",
            4 :  "Half Pullup",
            5 :  "Full Pullup",
            6 :  "Close",
            7 :  "Uneven Pullup",
            8 :  "1/2 One-Arm Pullup",
            9 :  "Assisted One-Arm Pullup",
            10 : "One-Arm Pullup"
        }
    },
    "hanging_leg_raise" : {
        "progressions" : {
            1 : "Knee Tuck",
            2 : "Knee Raise",
            3 : "Bent Leg Raise",
            4 : "Frog Leg Raise",
            5 : "Flat Leg Raise",
            6 : "Hanging Knee Raise",
            7 : "Hanging Bent Leg Raise",
            8 : "Hanging Frong Raise",
            9 : "Partial Leg Raise",
            10: "Hanging Leg Raise"
        }
    },
    "one-leg-squat" : {
        "progressions" : {
            1 : "Shoulderstand Squat",
            2:  "Jackknife Squat",
            3:  "Supported Squat",
            4:  "Half Squat",
            5:  "Full Squat",
            6:  "Close Squat",
            7:  "Uneven Squat",
            8:  "1/2 One-Leg Squat",
            9:  "Assisted One-Leg Squat",
            10: "One-leg Squat",

        }
    },
    "one-arm-pushup" : {
        "progressions" : {
            1 :"Wall Pushup",
            2: "Incline Pushup",
            3: "Kneeling Pushup",
            4: "Half Pushup",
            5: "Full Pushup",
            6: "Close Pushup",
            7: "Uneven Pushup",
            8: "1/2 One-Arm Pushup",
            9: "Lever Pushup",
            10:"One-Arm Pushup"

        }
    },
    "stand-to-stand-bridge" : {
        "progressions" : {
            1 :"Short Bridge",
            2: "Straight Bridge",
            3: "Angled Bridge",
            4: "Head Bridge",
            5: "Half Bridge",
            6: "Full Bridge",
            7: "Wall Walking Bridges Down",
            8: "Wall Walking Bridges Up",
            9: "Closing Bridge",
            10:"Stant-to-Stand Bridge"
        }
    },
    "one-arm-handstand-pushup" : {
        "progressions" : {
            1: "Wall Headstand",
            2: "Crow Stand",
            3: "Wall Handstand",
            4: "Half Handstand Pushup",
            5: "Handstand Pushup",
            6: "Close Handstand Pushup",
            7: "Uneven Handstand Pushup",
            8: "1/2 One-Arm Handstand Pushup",
            9: "Lever Handstand Pushup",
            10:"One-Arm Handstand Pushup"
        }
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
