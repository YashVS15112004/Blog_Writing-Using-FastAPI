from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import repository.blog
import schemas, models, database, repository, oauth2
from typing import List

router = APIRouter(tags=["Blogs"], prefix="/Blogs")

get_db = database.get_db
Blog = repository.blog


@router.post(
    "/Create", response_model=schemas.BlogOut, status_code=status.HTTP_201_CREATED
)
def createBlog(
    blog: schemas.CreateBlog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return Blog.createBlog(blog, db)


@router.get(
    "/Fetch", response_model=list[schemas.BlogOut], status_code=status.HTTP_200_OK
)
def returnBlogs(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return Blog.returnBlogs(db)


@router.get("/{id}", response_model=schemas.BlogOut, status_code=status.HTTP_200_OK)
def returnBlogByID(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return Blog.returnBlogByID(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(
    id: int,
    blog_req: schemas.CreateBlog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return Blog.update_blog(id, blog_req, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return Blog.delete_blog(id, db)
