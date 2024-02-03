from fastapi import FastAPI
#comment
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

@app.get("/")
async def root():
    return master_exercises

@app.get("/workouts/{id}")
async def root(id: int):
    if id == 1:
        return "yay you got this working"
    return {"This would be some workouts"}
