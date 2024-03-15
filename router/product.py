from fastapi import APIRouter, status
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router= APIRouter(
    prefix="/product", 
    tags=["product"]
    )

products= ["watch", "necklace", "bucket"]

@router.get("/all")
def get_all_products():
    data=" ".join(products)
    response=Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response
@router.get("/{id}", responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div> Product </div>"
                }
        },
        "description": "Returns the HTML of an object"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "product not found"
                           }
        },
        "description": "A plain text error message"
    }
}        
            )
def get_product(id: int):
    if id>len(products):
        out="product not found"
        return PlainTextResponse(status_code=status.HTTP_404_NOT_FOUND, content=out, media_type="text/plain")
    product= products[id]
    out= f"""
    <head>
    <style>
     .product {{
        width: 500px;
        height: 30px;
        border: 2px inset green;
        background-color: lightblue;
        text-align: center;
     }}    
     </style>
     </head>
     <div class= "product">{product}</div>
"""
    return HTMLResponse(status_code=status.HTTP_200_OK, content=out, media_type="text/html")