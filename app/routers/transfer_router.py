from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func
from .. import models, schemas
from ..database import get_db
from uuid import UUID
router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post("/", response_model=schemas.TransactionOut)
def make_transaction(transfer: schemas.MakeTransaction, db: Session = Depends(get_db)):
    new_transaction = models.Transfer(**transfer.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

@router.get("/{uuid}", response_model=schemas.TransactionOut)
def get_by_uuid(uuid: UUID, db: Session = Depends(get_db)):
    transaction = db.query(models.Transfer).filter(models.Transfer.uuid == uuid).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found any transaction with identifier {uuid}")
    return transaction