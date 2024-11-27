from fastapi import FastAPI
from routes import product, category

app = FastAPI()

app.include_router(product.router)
app.include_router(category.router)

@app.get("/")
def root():
    return {"message": "Witaj, dodaj /docs w linku :)"}
