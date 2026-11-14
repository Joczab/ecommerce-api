from fastapi import APIRouter

import src.models.product as product_models

from src.schemas.product import ProductCreate,ProductRead,ProductBase
from src.models.product import logger
from src.models.product import read_db, write_db

router = APIRouter(tags=['Products'])

@router.get('/products')
def get_products():
    
    data = product_models.get_products()
    if not data:
        return {}
    
    return data
    

@router.post('/products', response_model=ProductRead)
def create_products(product: ProductCreate):
    return product_models.create_product(product.model_dump())


    
@router.put('/products/{product_id}')
def update_product(product_id: int, changes:dict )