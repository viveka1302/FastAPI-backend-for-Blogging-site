from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import shutil

router = APIRouter(
    prefix="/file",
    tags=["file"]
)

@router.post("/get")
def get_file(file: bytes= File(...)):
    content= file.decode('utf-8')
    lines=content.split('/n')
    return {"lines": lines}

@router.post("/uploadFile")
def upload_file(uploadFile: UploadFile= File(...)):
    path= f"files/{uploadFile.filename}" #If two files have the same name the first file will be overwritten.
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(uploadFile.file, buffer)

    return {
        "filename": path,
        "type": uploadFile.content_type
            }

@router.get("/download/{name}", response_class=FileResponse)
def get_file(name: str):
    path= f'files/{name}'
    return path
    