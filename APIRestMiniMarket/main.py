from fastapi import FastAPI
from starlette.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.producto import producto_router
from routers.user import user_router

app = FastAPI()
app.title = "Tienda la holandesa"
app.version = "0.0.1.1"

app.add_middleware(ErrorHandler)

app.include_router(producto_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Tienda la holandesa</h1>')