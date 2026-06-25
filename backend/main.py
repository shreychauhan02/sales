from fastapi import FastAPI

from database import engine
from models import Base

from routes.customer import router as customer_router
from routes.category import router as category_router
from routes.product import router as product_router
from routes.employee import router as employee_router
from routes.order import router as order_router
from routes.analytics import router as analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sales Management System"
)

app.include_router(customer_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(employee_router)
app.include_router(order_router)
app.include_router(analytics_router)

@app.get("/")
def home():
    return {"message": "Sales Management API Running"}