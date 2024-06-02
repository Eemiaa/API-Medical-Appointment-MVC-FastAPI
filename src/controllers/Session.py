from fastapi import APIRouter, status

router = APIRouter(
    prefix="/session",
    tags=['Session']
)

class SessionController:

    @router.get("/hello/", status_code=status.HTTP_200_OK) #response_model
    async def hello_world():
        return {"hello":"world"}