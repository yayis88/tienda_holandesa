from fastapi import APIRouter, Depends, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.producto import ProductoService
from schemas.producto import Producto

producto_router = APIRouter()

@producto_router.get('/productos', tags=['productos'], response_model=List[Producto], status_code=200)
def get_productos() -> List[Producto]:
    db = Session()
    try:
        result = ProductoService(db).get_productos()
    finally:
        db.close()
    return result

@producto_router.get('/productos/{id}', tags=['productos'], response_model=Producto)
def get_producto(id: int = Path(..., ge=1, le=2000)) -> Producto:
    db = Session()
    try:
        result = ProductoService(db).get_producto(id)
        if not result:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
    finally:
        db.close()
    return result

@producto_router.get('/productos/', tags=['productos'], response_model=List[Producto])
def get_productos_by_category(category: str = Query(..., min_length=4, max_length=20)) -> List[Producto]:
    db = Session()
    try:
        result = ProductoService(db).get_productos_by_category(category)
    finally:
        db.close()
    return result

@producto_router.post('/productos', tags=['productos'], response_model=dict, status_code=201)
def create_producto(producto: Producto) -> dict:
    db = Session()
    try:
        ProductoService(db).create_producto(producto)
        db.commit()
    finally:
        db.close()
    return {"mensaje": "Se ha registrado el producto"}

@producto_router.put('/productos/{id}', tags=['productos'], response_model=dict, status_code=200)
def update_producto(id: int, producto: Producto) -> dict:
    db = Session()
    try:
        result = ProductoService(db).get_producto(id)
        if not result:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        ProductoService(db).update_producto(id, producto)
        db.commit()
    finally:
        db.close()
    return {"message": "Se ha modificado el producto"}

@producto_router.delete('/productos/{id}', tags=['productos'], response_model=dict, status_code=200)
def delete_producto(id: int) -> dict:
    db = Session()
    try:
        result = ProductoService(db).get_producto(id)
        if not result:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        ProductoService(db).delete_producto(id)
        db.commit()
    finally:
        db.close()
    return {"message": "Se ha eliminado el producto"}