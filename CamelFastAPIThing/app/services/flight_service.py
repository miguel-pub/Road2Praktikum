from sqlalchemy.orm import Session
from ..models.flight import Flight
from ..schemas.flight import FlightCreate
from datetime import datetime

class FlightService:
    @staticmethod
    async def create_flight(db: Session, flight_data: FlightCreate) -> Flight:
        db_flight = Flight(
            flight_id=flight_data.flight_id,
            departure_airport=flight_data.departure_airport,
            arrival_airport=flight_data.arrival_airport,
            scheduled_departure=flight_data.scheduled_departure,
            scheduled_arrival=flight_data.scheduled_arrival,
            status=flight_data.status,
            position_data=flight_data.position_data.dict(),
            telemetry_data=flight_data.telemetry_data.dict(),
            weather_data=flight_data.weather_data.dict()
        )
        db.add(db_flight)
        db.commit()
        db.refresh(db_flight)
        return db_flight

    @staticmethod
    async def get_flight(db: Session, flight_id: str) -> Flight:
        return db.query(Flight).filter(Flight.flight_id == flight_id).first()