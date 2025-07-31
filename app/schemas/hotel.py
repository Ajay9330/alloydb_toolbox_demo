from pydantic import BaseModel

class HotelBase(BaseModel):
    name: str
    address: str
    city: str
    state: str
    country: str
    phonenumber: str
    email: str
    rating: float

class HotelCreate(HotelBase):
    pass

class Hotel(HotelBase):
    hotelid: int

    class Config:
        from_attributes = True
