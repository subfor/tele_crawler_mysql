import datetime
import asyncio
import aiomysql

from pytz import timezone
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

TIMEZONE = timezone('Europe/Kiev')

DeclarativeBase = declarative_base()


def time_now():
    return datetime.datetime.now(TIMEZONE)


class AuctionData(DeclarativeBase):
    __tablename__ = 'auction_data'

    id = Column(Integer, primary_key=True)
    creation_time = Column('creation_time', DateTime(timezone=True), default=time_now)
    date = Column('date', String(20))
    position = Column('position', String(10))
    seller = Column('seller', String(100))
    goods = Column('goods', String(100))
    kind = Column('kind', Text)
    delivery_basis = Column('delivery_basis', String(20))
    place = Column('place', String(100))
    transport = Column('transport', String(100))
    lot_count = Column('lot_count', String(20))
    value = Column('value', String(20))
    min_price = Column('min_price', String(30))
    max_price = Column('max_price', String(30))
    average_price = Column('average_price', String(30))

    def __repr__(self):
        return "".format(self.code)


async def create_tables():
    engine = create_async_engine(
        "mysql+aiomysql://root:pass@192.168.3.5:3310/auction_data", echo=False,
    )
    async with engine.begin() as conn:
        await conn.run_sync(AuctionData.metadata.drop_all)
        await conn.run_sync(AuctionData.metadata.create_all)
    await engine.dispose()


async def write_to_db(data: list):
    engine = create_async_engine(
        "mysql+aiomysql://root:pass@192.168.3.5:3310/auction_data", echo=False,
    )
    async with engine.begin() as conn:
        await conn.execute(AuctionData.__table__.insert(), data)
    await engine.dispose()


if __name__ == '__main__':
    asyncio.run(create_tables())
