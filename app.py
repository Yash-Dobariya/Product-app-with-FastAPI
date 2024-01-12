from fastapi import FastAPI
from src.api.user import user_route
from src.api.admin import admin_route
from src.api.product import product_route
import uvicorn


app = FastAPI()

app.include_router(user_route)
app.include_router(admin_route)
app.include_router(product_route)

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=3000, reload=True)
