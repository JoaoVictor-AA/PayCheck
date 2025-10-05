from fastapi import FastAPI
import uvicorn
from app.database import engine
import app.models as models
from .routers import user_route
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.add_route(user_route.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
