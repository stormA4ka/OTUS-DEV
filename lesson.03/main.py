from fastapi import FastAPI, Request, APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional

# uvicorn main:app --reload
# http://127.0.0.1:8000/docs

app = FastAPI()

# Подключаем шаблоны
templates = Jinja2Templates(directory="templates")

# Подключаем статику
app.mount("/static", StaticFiles(directory="static"), name="static")

# Создаем API роутер с префиксом /api
api_router = APIRouter(prefix="/api")

# Пример данных для товаров
products = [
    {"id": 1, "name": "Product 1", "description": "Description 1"},
    {"id": 2, "name": "Product 2", "description": "Description 2"},
]

# Модель данных для товара
class Product(BaseModel):
    id: int
    name: str
    description: str

# Вложенный роутер для сущности "товар"
products_router = APIRouter(prefix="/products")

# Представление для чтения списка товаров
@products_router.get("/", response_model=List[Product])
async def read_products():
    return products

# Представление для чтения одного товара
@products_router.get("/{product_id}", response_model=Product)
async def read_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Представление для создания товара
@products_router.post("/", response_model=Product)
async def create_product(product: Product):
    products.append(product.dict())
    return product

# Подключаем вложенный роутер к API роутеру
api_router.include_router(products_router)

# Подключаем API роутер к основному приложению
app.include_router(api_router)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/about/", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})