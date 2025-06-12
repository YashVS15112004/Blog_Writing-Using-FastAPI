from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import repository.user
import schemas, models, database, repository,oauth2
from typing import List
from hashing import hash_password

router = APIRouter(tags=["Users"], prefix="/Users")
get_db = database.get_db
User = repository.user


@router.post(
    "/Create",
    response_model=schemas.UserOut,
    status_code=status.HTTP_200_OK,
)
def createUser(user: schemas.UserCreate, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return User.createUser(user, db)


@router.get(
    "/{id}",
    response_model=schemas.UserOut,
    status_code=status.HTTP_200_OK,
)
def getUser(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return User.getUser(id, db)
