from fastapi import FastAPI
import uvicorn
from app.database import engine
import app.models as models
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def test_runner():
    return {"The greatest pleasure?": "When you break his ego."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
