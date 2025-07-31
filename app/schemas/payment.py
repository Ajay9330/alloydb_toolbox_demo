from pydantic import BaseModel, field_validator
from datetime import date, datetime

class PaymentBase(BaseModel):
    bookingid: int
    amount: float
    paymentdate: date
    paymentmethod: str

    @field_validator("paymentdate", mode="before")
    def convert_datetime_to_date(cls, value):
        if isinstance(value, datetime):
            return value.date()
        return value

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    paymentid: int

    class Config:
        from_attributes = True
