from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship

from database import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    phone_number = Column(Text)


class Category(Base):
    __tablename__ = "category"

    cat_id = Column(Integer, primary_key=True, index=True)
    cat_name = Column(String(255), nullable=False)
    cat_rel_id = Column(Integer, nullable=False)


class Product(Base):
    __tablename__ = "product"

    p_id = Column(Integer, primary_key=True, index=True)
    p_name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey("category.cat_id"))
    price = Column(Integer, nullable=False)
    stock = Column(Integer)

    category = relationship("Category")


class Employee(Base):
    __tablename__ = "employee"

    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String(255), nullable=False)


class Orders(Base):
    __tablename__ = "orders"

    o_id = Column(Integer, primary_key=True, index=True)
    order_date = Column(Date)
    total_price = Column(Integer)
    status = Column(Text)

    cus_id = Column(Integer, ForeignKey("customer.id"))
    emp_id = Column(Integer, ForeignKey("employee.emp_id"))

    customer = relationship("Customer")
    employee = relationship("Employee")


class OrderItem(Base):
    __tablename__ = "order_item"

    item_id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer, ForeignKey("orders.o_id"))
    product_id = Column(Integer, ForeignKey("product.p_id"))

    amount = Column(Integer)
    discount = Column(Integer)

    order = relationship("Orders")
    product = relationship("Product")