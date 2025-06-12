from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, models, database
from typing import List
from hashing import hash_password

get_db = database.get_db


def createUser(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashedPassword = hash_password(user.password)
    db_user = models.User(name=user.name, email=user.email, password=hashedPassword)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def getUser(id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail=f"User with ID {id} not found")
    return db_user
