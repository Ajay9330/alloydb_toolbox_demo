from fastapi import APIRouter
from app.api.endpoints import hotels, rooms, guests, bookings, payments, room_types

api_router = APIRouter()
api_router.include_router(hotels.router, prefix="/hotels", tags=["hotels"])
api_router.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
api_router.include_router(guests.router, prefix="/guests", tags=["guests"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])
api_router.include_router(room_types.router, prefix="/room_types", tags=["room_types"])
