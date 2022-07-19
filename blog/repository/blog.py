from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from blog import models
from blog.database import get_db
from blog.schemas import Blog, UpdateBlog


def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blogs Not Found")
    return blogs


def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(**request.dict(), user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_by_id(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).where(models.Blog.id == id).first()
    if blog:
        return blog
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with the id {id} is not available")


def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    blog.delete(synchronize_session=False)
    db.commit()
    return "Deleted"


def update(id: int, request: UpdateBlog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Blog with the id {id} is not available")
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return "Updated"
