from fastapi import APIRouter, status

router = APIRouter(
    prefix="/session",
    tags=['Session']
)

@router.get("/hello/", status_code=status)
async def hello_world():
    return {"hello":"world"}