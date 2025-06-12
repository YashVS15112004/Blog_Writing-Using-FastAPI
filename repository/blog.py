from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas,models,database
from typing import List

get_db = database.get_db


def createBlog(blog: schemas.CreateBlog, db: Session = Depends(get_db)):
    db_blog = models.Blog(title=blog.title, body=blog.body, user_id=blog.user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def returnBlogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()


def returnBlogByID(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )
    return blog


def update_blog(id: int, blog_req: schemas.CreateBlog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found"
        )
    blog.update(blog_req.dict())
    db.commit()
    return {"message": f"Blog with ID {id} updated successfully"}


def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with ID {id} not found")
    db.delete(blog)
    db.commit()
