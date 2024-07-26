from sqlalchemy.orm import Session
from models.producto import Producto as ProductoModel
from schemas.producto import Producto

class ProductoService:
    def __init__(self, db: Session):
        self.db = db

    def get_productos(self):
        return self.db.query(ProductoModel).all()

    def get_producto(self, id: int):
        return self.db.query(ProductoModel).filter(ProductoModel.id == id).first()

    def get_productos_by_category(self, category: str):
        return self.db.query(ProductoModel).filter(ProductoModel.category == category).all()

    def create_producto(self, producto: Producto):
        new_producto = ProductoModel(**producto.dict())
        self.db.add(new_producto)

    def update_producto(self, id: int, producto: Producto):
        existing_producto = self.db.query(ProductoModel).filter(ProductoModel.id == id).first()
        if existing_producto:
            for key, value in producto.dict().items():
                setattr(existing_producto, key, value)
            self.db.add(existing_producto)

    def delete_producto(self, id: int):
        existing_producto = self.db.query(ProductoModel).filter(ProductoModel.id == id).first()
        if existing_producto:
            self.db.delete(existing_producto)
