from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from prediction import predict

class sensor_readings(BaseModel):
    pm2: float
    PM10: float
    NO: float
    NO2: float
    NOx: float
    NH3: float
    CO: float
    SO2: float
    O3: float
    Benzene: float
    Toluene: float
    Xylene: float

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def test():
    return {"message": "API WORKING"}

@app.post("/aqi")
async def getaqi(sensor_readings: sensor_readings):
    return predict({
    "PM2.5" :   sensor_readings.pm2,
    "PM10"  :   sensor_readings.PM10,
    "NO"    :   sensor_readings.NO,
    "NO2"   :   sensor_readings.NO2,
    "NOx"   :   sensor_readings.NOx,
    "NH3"   :   sensor_readings.NH3,
    "CO"    :   sensor_readings.CO,
    "SO2"   :   sensor_readings.SO2,
    "O3"    :   sensor_readings.O3,
    "Benzene"   :   sensor_readings.Benzene,
    "Toluene"   :   sensor_readings.Toluene,
    "Xylene"    :   sensor_readings.Xylene,
    })