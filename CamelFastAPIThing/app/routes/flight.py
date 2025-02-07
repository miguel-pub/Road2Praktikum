from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..schemas.flight import FlightCreate, FlightInDB
from ..services.flight_service import FlightService
import xml.etree.ElementTree as ET
from ..core.config import settings

router = APIRouter()

@router.post("/flights/", response_model=FlightInDB)
async def create_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    try:
        tree = ET.parse(settings.CAMEL_ROUTE_PATH)
        root = tree.getroot()
                # Access the root element's tag
        print(f"Root element: {root.tag}")  # Output: Root element: routes

        # Access attributes of the root element
        print(f"Root attributes: {root.attrib}")  # Output: Root attributes: {'xmlns': 'http://camel.apache.org/schema/spring'}

        # Find the first 'route' element
        route = root.find('route')
        if route is not None:
            print(f"Route ID: {route.attrib['id']}")  # Output: Route ID: flightDataRoute
            
        return await FlightService.create_flight(db=db, flight_data=flight)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/flights/{flight_id}", response_model=FlightInDB)
async def read_flight(flight_id: str, db: Session = Depends(get_db)):
    flight = await FlightService.get_flight(db=db, flight_id=flight_id)
    if flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight