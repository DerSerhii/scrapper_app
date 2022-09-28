from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Rent(Base):
    __tablename__ = 'Rents'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    image = Column(String)
    city = Column(String)
    date = Column(String)
    beds = Column(String)
    description = Column(String)
    price = Column(Float, nullable=True)
    currency = Column(String, nullable=True)


if __name__ == '__main__':
    # Migrate
    # Create TABLE in database

    from settings import DB_PATH

    engine = create_engine(DB_PATH, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    session.commit()
