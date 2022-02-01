from fastapi import FastAPI
from routers import fibonacci

app = FastAPI()
app.include_router(fibonacci.router, prefix="/api/v1")
