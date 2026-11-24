from fastapi import FastAPI

app = FastAPI(title="Price Tracker API")


@app.get("/")
def root():
    return {"message": "Price Tracker API"}


@app.get("/products")
def list_products():
    # TODO: truy vấn từ database
    return []
