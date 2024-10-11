from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Date, Float, Integer, BigInteger, ForeignKey
# import sqlalchemy.types

class BaseModel(DeclarativeBase):
    pass

class Motorist(BaseModel):
    __tablename__ = 'motorist'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))


class Cars(BaseModel):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(primary_key=True)
    make_model: Mapped[str] = mapped_column(String(30))
    car_year: Mapped[datetime.date] = mapped_column(Date())
    mileage: Mapped[int] = mapped_column(BigInteger())
    engine_displace: Mapped[float] = mapped_column(Float())
    engine_type: Mapped[str] = mapped_column(String(15))
    oil_change_data: Mapped[datetime.date] = mapped_column(Date())
    air_filter_change_data: Mapped[datetime.date] = mapped_column(Date())

