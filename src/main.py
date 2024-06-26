from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controllers import SessionController
origins = ["*"]

def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(SessionController.router)
    return app

app = create_app()

if __name__ == "__main__":  
    import uvicorn 
    uvicorn.run(app, host="localhost", port=8000)