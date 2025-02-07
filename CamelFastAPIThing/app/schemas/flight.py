from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict, Any, Optional

class PositionData(BaseModel):
    latitude: float
    longitude: float
    altitude: float

class TelemetryData(BaseModel):
    speed: float
    heading: float
    vertical_speed: Optional[float] = None

class WeatherData(BaseModel):
    temperature: float
    wind_speed: float
    wind_direction: float

class FlightBase(BaseModel):
    flight_id: str = Field(..., description="Unique flight identifier")
    departure_airport: str = Field(..., min_length=3, max_length=3)
    arrival_airport: str = Field(..., min_length=3, max_length=3)
    scheduled_departure: datetime
    scheduled_arrival: datetime
    status: str
    position_data: PositionData
    telemetry_data: TelemetryData
    weather_data: WeatherData

class FlightCreate(FlightBase):
    pass

class FlightInDB(FlightBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True