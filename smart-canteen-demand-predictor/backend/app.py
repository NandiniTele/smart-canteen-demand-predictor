from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_demand
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionInput(BaseModel):
    day: str
    meal: str
    item: str
    weather: str
    event: str


@app.get("/")
def home():
    return {"message": "Smart Canteen Demand Predictor"}


@app.post("/predict")
def predict(data: PredictionInput):

    result = predict_demand(
        data.day,
        data.meal,
        data.item,
        data.weather,
        data.event
    )

    if "error" in result:
        return {"error": result["error"]}

    return {"predicted_demand": result["demand"]}