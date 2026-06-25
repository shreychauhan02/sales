from fastapi import APIRouter
from sqlalchemy import text

from database import engine

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/top-products")
def top_products():

    query = """
    SELECT
        p.p_name,
        SUM(o.amount) AS total_sales
    FROM product p
    INNER JOIN order_item o
    ON p.p_id = o.product_id
    GROUP BY p.p_id,p.p_name
    ORDER BY total_sales DESC
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))

    return [dict(row._mapping) for row in result]



@router.get("/top-customers")
def top_customers():

    query = """
    SELECT
        c.name,
        COUNT(o.o_id) AS total_orders
    FROM customer c
    INNER JOIN orders o
    ON c.id=o.cus_id
    GROUP BY c.id,c.name
    ORDER BY total_orders DESC
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))

    return [dict(row._mapping) for row in result]



@router.get("/top-customers")
def top_customers():

    query = """
    SELECT
        c.name,
        COUNT(o.o_id) AS total_orders
    FROM customer c
    INNER JOIN orders o
    ON c.id=o.cus_id
    GROUP BY c.id,c.name
    ORDER BY total_orders DESC
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))

    return [dict(row._mapping) for row in result]


@router.get("/category-revenue")
def category_revenue():

    query = """
    SELECT
        c.cat_name,
        SUM(p.price * oi.amount) AS revenue
    FROM category c
    JOIN product p
        ON c.cat_id = p.category_id
    JOIN order_item oi
        ON p.p_id = oi.product_id
    GROUP BY c.cat_name
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))

    return [dict(row._mapping) for row in result]


@router.get("/top-employees")
def top_employees():

    query = """
    SELECT
        e.emp_name,
        COUNT(o.o_id) AS total_orders
    FROM employee e
    INNER JOIN orders o
        ON e.emp_id = o.emp_id
    GROUP BY e.emp_id,e.emp_name
    ORDER BY total_orders DESC
    LIMIT 5
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))

    return [dict(row._mapping) for row in result]


@router.get("/monthly-sales")
def monthly_sales():

    query = """
    SELECT
        MONTH(order_date) AS month,
        SUM(total_price) AS sales
    FROM orders
    GROUP BY MONTH(order_date)
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))

    return [dict(row._mapping) for row in result]