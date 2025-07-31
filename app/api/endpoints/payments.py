from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import payments as payment_model
from app.schemas import payment as payment_schema
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=payment_schema.Payment)
def create_payment(payment: payment_schema.PaymentCreate, db: Session = Depends(get_db)):
    try:
        db_payment = payment_model.Payment(**payment.model_dump())
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
        return db_payment
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create payment: {e}")

@router.get("/{payment_id}", response_model=payment_schema.Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = db.query(payment_model.Payment).filter(payment_model.Payment.paymentid == payment_id).first()
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.get("", response_model=List[payment_schema.Payment])
def read_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments = db.query(payment_model.Payment).offset(skip).limit(limit).all()
    return payments
