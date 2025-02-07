from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func
from ..core.database import Base

class Flight(Base):
    __tablename__ = "flights"
    
    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(String, index=True)
    departure_airport = Column(String(3))
    arrival_airport = Column(String(3))
    scheduled_departure = Column(DateTime(timezone=True))
    scheduled_arrival = Column(DateTime(timezone=True))
    status = Column(String)
    position_data = Column(JSON)
    telemetry_data = Column(JSON)
    weather_data = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())