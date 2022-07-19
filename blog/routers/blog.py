from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas, oauth2, token
from blog.database import get_db
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)


@router.get("/", response_model=List[schemas.ShowBlog])
async def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_blog(request: schemas.Blog, db: Session = Depends(get_db),
                      current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db, current_user)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
async def get_by_id(id: int, db: Session = Depends(get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_by_id(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: schemas.UpdateBlog, db: Session = Depends(get_db),
                 current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
