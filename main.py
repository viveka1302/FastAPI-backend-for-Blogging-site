from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from router import file
from templates import templates
from auth import authentication
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app= FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(file.router)
app.include_router(templates.router)

#custom exception handler
@app.exception_handler(StoryException)
def story_exception_handler(req: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail": exc.name}
    )

models.Base.metadata.create_all(engine)

#this block of code will ALLOW backend to interact with frontend on the same machine.
origins= [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers=["*"]
)

app.mount("/files", StaticFiles(directory='files'), name='files')