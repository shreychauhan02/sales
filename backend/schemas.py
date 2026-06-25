from pydantic import BaseModel, Field
from datetime import date



class CustomerBase(BaseModel):
    name: str = Field(
        ...,
        title="Customer Name",
        description="Full name of the customer.",
        examples=["Alice Johnson", "Ravi Patel"],
    )
    phone_number: str = Field(
        ...,
        title="Phone Number",
        description="Customer's contact phone number",
        examples=["+91-9876543210"],
    )

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int = Field(
        ...,
        title="Customer ID",
        description="Auto-generated unique identifier for the customer.",
        examples=[1, 42],
    )

    class Config:
        from_attributes = True



class CategoryBase(BaseModel):
    cat_name: str = Field(
        ...,
        title="Category Name",
        description="Display name of the product category.",
        examples=["Electronics", "Clothing", "Home & Garden"],
    )
    cat_rel_id: int = Field(
        ...,
        title="Related Category ID",
        description="ID of the parent or related category (use 0 for top-level).",
        examples=[0, 3, 7],
    )

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    cat_id: int = Field(
        ...,
        title="Category ID",
        description="Auto-generated unique identifier for the category.",
        examples=[1, 5, 12],
    )

    class Config:
        from_attributes = True



class ProductBase(BaseModel):
    p_name: str = Field(
        ...,
        title="Product Name",
        description="Full name or title of the product.",
        examples=["Wireless Headphones", "Men's Running Shoes", "LED Desk Lamp"],
    )
    category_id: int = Field(
        ...,
        title="Category ID",
        description="ID of the category this product belongs to.",
        examples=[2, 5],
    )
    price: int = Field(
        ...,
        title="Price",
        description="Product price in the smallest currency unit (e.g. paise or cents).",
        examples=[49900, 1299, 85000],
    )
    stock: int = Field(
        ...,
        title="Stock Quantity",
        description="Number of units currently available in inventory.",
        examples=[100, 0, 250],
    )

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    p_id: int = Field(
        ...,
        title="Product ID",
        description="Auto-generated unique identifier for the product.",
        examples=[1, 17, 204],
    )

    class Config:
        from_attributes = True



class EmployeeBase(BaseModel):
    emp_name: str = Field(
        ...,
        title="Employee Name",
        description="Full name of the employee.",
        examples=["Priya Sharma", "James Carter"],
    )

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    emp_id: int = Field(
        ...,
        title="Employee ID",
        description="Auto-generated unique identifier for the employee.",
        examples=[1, 8, 23],
    )

    class Config:
        from_attributes = True



class OrderBase(BaseModel):
    order_date: date = Field(
        ...,
        title="Order Date",
        description="Date the order was placed (YYYY-MM-DD).",
        examples=["2024-06-15", "2025-01-01"],
    )
    total_price: int = Field(
        ...,
        title="Total Price",
        description="Total cost of the order in the smallest currency unit.",
        examples=[149900, 5000, 320000],
    )
    status: str = Field(
        ...,
        title="Order Status",
        description="Current state of the order.",
        examples=["pending", "confirmed", "shipped", "delivered", "cancelled"],
    )
    cus_id: int = Field(
        ...,
        title="Customer ID",
        description="ID of the customer who placed this order.",
        examples=[1, 7],
    )
    emp_id: int = Field(
        ...,
        title="Employee ID",
        description="ID of the employee handling this order.",
        examples=[3, 11],
    )

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    o_id: int = Field(
        ...,
        title="Order ID",
        description="Auto-generated unique identifier for the order.",
        examples=[1001, 2048],
    )

    class Config:
        from_attributes = True


class OrderItemBase(BaseModel):
    order_id: int = Field(
        ...,
        title="Order ID",
        description="ID of the parent order this item belongs to.",
        examples=[1001, 2048],
    )
    product_id: int = Field(
        ...,
        title="Product ID",
        description="ID of the product included in this line item.",
        examples=[17, 204],
    )
    amount: int = Field(
        ...,
        title="Quantity",
        description="Number of units of the product ordered.",
        examples=[1, 3, 10],
    )
    discount: int = Field(
        ...,
        title="Discount",
        description="Discount applied to this line item in the smallest currency unit.",
        examples=[0, 500, 1000],
    )

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    item_id: int = Field(
        ...,
        title="Order Item ID",
        description="Auto-generated unique identifier for this order line item.",
        examples=[1, 5, 99],
    )

    class Config:
        from_attributes = True