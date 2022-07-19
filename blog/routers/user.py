from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog import schemas
from blog.database import get_db
from blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/", response_model=List[schemas.ShowUser])
async def get_all(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.post("/")
async def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
async def get_by_id(id: int, db: Session = Depends(get_db)):
    return user.get_by_id(id, db)
