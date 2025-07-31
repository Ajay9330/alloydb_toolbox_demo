from pydantic import BaseModel, field_validator
from datetime import date, datetime

class BookingBase(BaseModel):
    guestid: int
    roomid: int
    checkindate: date
    checkoutdate: date
    totalprice: float
    status: str

    @field_validator("checkindate", "checkoutdate", mode="before")
    def convert_datetime_to_date(cls, value):
        if isinstance(value, datetime):
            return value.date()
        return value

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    bookingid: int

    class Config:
        from_attributes = True
