import http
from optparse import Option
from token import COMMENT
from fastapi import APIRouter, status,Response
from typing import Optional
from enum import Enum

router= APIRouter(prefix="/blog", tags=["blog"])

@router.get(
    "/all",
    summary="retreives all blogs",
    description="An API to simulate retreival of all blogs",
    response_description="A list of all blogs"
            )
def get_all_blogs(page=1, page_size: Optional[int]= None):
    return {"message": f"All {page_size} blogs on {page}"}

@router.get(
    "/{id}/comments/{comment_id}",
    tags=["comments"]
    )
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str]= None):
    """
    Simulates receiving comment of a blog
    **id** - Mandatory path parameter
    **comment_id** - Mandatory path parameter
    **valid** - Optional query parameter
    **username** - Optional query parameter
    """
    return {"message": f"blog ID:{id}, comment ID: {comment_id}, valid: {valid}, username: {username}"}

class BlogType(str, Enum):
    short= "short"
    story= "story"
    howto= "howto"
    
@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog Type {type}"}

@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_id(id: int, response: Response):
    if id>5:
        response.status_code= status.HTTP_404_NOT_FOUND
        return {"message": f"blog_id {id} not found"}
    else:
        response.status_code= status.HTTP_200_OK
        return {"message": f"blog_ID = {id}"}

