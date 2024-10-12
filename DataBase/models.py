from sqlalchemy import Table, Column, ForeignKey, String, Text, Date, Float, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime


BaseModel = declarative_base()


class Motorist(BaseModel):
    __tablename__ = 'motorist'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    user_id = Column(Integer, nullable=False)


cars_goodbuy = Table('cars_goodbuy', BaseModel.metadata,
                     Column('car_id', Integer(), ForeignKey('cars.id')),
                     Column('goodbuy_id', Integer(), ForeignKey('goodbuy.id')))

cars_costs = Table('cars_costs', BaseModel.metadata,
                   Column('car_id', Integer(), ForeignKey('cars.id')),
                   Column('cost_id', Integer(), ForeignKey('costs.id')))

cars_shopping_plan = Table('cars_shopping_plan', BaseModel.metadata,
                           Column('car_id', Integer(), ForeignKey('cars.id')),
                           Column('shopping_plan_id', Integer(), ForeignKey('shopping_plan.id')))


class Cars(BaseModel):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make_model = Column(String(30), nullable=False)
    car_year = Column(Date, default=datetime.date(2000, 1, 1))
    mileage = Column(BigInteger)
    engine_distance = Column(Float)
    engine_type = Column(String(15))
    oil_change_data = Column(Date)
    air_filter_change_data = Column(Date)
    motorist_id = Column(Integer, ForeignKey('motorist.id'))
    motorist = relationship('Motorist', backref='cars_motorist')
    goodbuy = relationship('GoodBuy', secondary=cars_goodbuy, backref='cars_goodbuy')
    costs = relationship('Costs', secondary=cars_costs, backref='cars_costs')
    shopping_plan = relationship('ShoppingPlan', secondary=cars_shopping_plan, backref='cars_shopping_plan')


class GoodBuy(BaseModel):
    __tablename__ = 'goodbuy'
    id = Column(Integer, primary_key=True)
    purchase_date = Column(Date)
    price = Column(Float, nullable=False)
    vendor_contacts = Column(Text, nullable=False)
    photo = Column(String(255), nullable=False)
    cars = relationship('Cars', secondary=cars_goodbuy, backref='goodbuy')


class Costs(BaseModel):
    __tablename__ = 'costs'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    unit_price = Column(Float, nullable=False)
    purchase_date = Column(Date)
    cars = relationship('Cars', secondary=cars_costs, backref='costs')


class ShoppingPlan(BaseModel):
    __tablename__ = 'shopping_plan'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(String(4))
    cars = relationship('Cars', secondary=cars_shopping_plan, backref='shopping_plan')

