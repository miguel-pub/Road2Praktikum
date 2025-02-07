from fastapi import FastAPI
from app.routes import flight
from app.core.database import engine, Base
from app.core.config import settings

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Flight Tracking System")

# Include routers
app.include_router(
    flight.router,
    prefix=settings.API_PREFIX,
    tags=["flights"]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)