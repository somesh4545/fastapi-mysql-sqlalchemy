from fastapi import FastAPI
from routes.index import userRouter
from config.db import get_db, engine
import models.index as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def backend_testing():
    return {'msg', 'backend is running'}

app.include_router(userRouter, prefix='/user')