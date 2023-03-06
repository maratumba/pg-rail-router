from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class Coordinates(BaseModel):
    lat: float
    lng: float


class RouteCoordinates(BaseModel):
    origin: Optional[Coordinates]
    destination: Optional[Coordinates]


class Route(BaseModel):
    distance: float
    electrification_percentage: Optional[float]
    cached_at: Optional[datetime]
    coordinates: Optional[RouteCoordinates]


class RouteRequest(BaseModel):
    start: Coordinates
    end: Coordinates

