from fastapi import FastAPI

from routers import huggingface, students

app = FastAPI()

app.include_router(students.router)
app.include_router(huggingface.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

