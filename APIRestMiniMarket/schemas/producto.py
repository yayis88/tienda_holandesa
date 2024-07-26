from pydantic import BaseModel, Field
from typing import Optional

class Producto(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=50)
    precio: int
    category: str
    marca: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Nombre del producto",
                "precio": 00000,
                "category": "Categoria del producto",
                "marca": "Marca del producto"
            }
        }