from fastapi import APIRouter

order_router = APIRouter()

order_router = APIRouter(
    prefix='/orders',
    tags=['orders']
)

@order_router.get('/')
async def hello():
    return {'message': 'order Hello, world'}