import os
from typing import Optional
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/example")
def read_example():
    return {"data": "This is data coming from the example endpoint running on the api as a seperate microservice!"}