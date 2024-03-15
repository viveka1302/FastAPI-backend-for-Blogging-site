
from fastapi import APIRouter, status, Response, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List

router= APIRouter(prefix="/blog", tags= ["blog"])

class BlogModel(BaseModel):
    title: str
    content: str
    number_of_comments: int
    published: Optional[bool]
    tags: List[str] =[]
    metadata: dict[str, str]= {"key1": "val1"}

@router.post("/new/{id}")
def create_blog(id: int, blog: BlogModel, version: int= 1):
    return {
        "id": id,
        "data": blog,
        "version": version
        }
#everything passed in Body(), Query(), Path() are called VALIDATORS
# Body(...) is an ellipsis,i.e., it specifies Compulsory parameter
#validators for integers/floats are ge=, gt=, lt=, le=
@router.post("/new/{id}/comment/{comment_id}")
def create_comment(id: int, blog: BlogModel, comment_title: str= Query(
    None,
    alias= "comment Title",
    title= "Title of the comment",
    description= "Some description",
    deprecated=True
    ),
                   content: str= Body(...,
                                      min_length=10,
                                      max_length=50),
                   version: Optional[List[str]]= Query(['1.0','1.1','1.2']),
                   comment_id: int= Path(gt=5, le=10)
                   ):
    return {
        "id": id,
        "blog": blog,
        "comment Title": comment_title,
        "content": content,
        "version": version,
        "comment_id": comment_id
        }