import pickle
import pandas as pd

model = pickle.load(open("model.pkl","rb"))
encoders = pickle.load(open("encoders.pkl","rb"))

def predict_demand(day,meal,item,weather,event):

    try:
        input_data = {
            "day": encoders["day"].transform([day])[0],
            "meal": encoders["meal"].transform([meal])[0],
            "item": encoders["item"].transform([item])[0],
            "weather": encoders["weather"].transform([weather])[0],
            "event": encoders["event"].transform([event])[0]
        }
    except ValueError as e:
        return {"error": f"Invalid input category: {str(e)}"}

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]

    return {"demand": int(prediction)}