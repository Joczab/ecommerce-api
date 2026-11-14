from fastapi import APIRouter

from src.routes.products import router as products_router

router = APIRouter()
router.include_router(products_router)