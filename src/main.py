from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import Session
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

    app.include_router(Session.router)
    return app

app = create_app()

if __name__ == "__main__":  
    import uvicorn 
    uvicorn.run(app, host="localhost", port=8000)