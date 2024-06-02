from fastapi import FastAPI

def create_app():
    app = FastAPI(__name__)
    #app.config.from_object('config')
    app.router.inclued
    return app

app = create_app()