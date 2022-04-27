from sqlalchemy import Column, Integer, Text, null
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PetModel(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Customer: (id={self.id},first_name={self.first_name},last_name={self.last_name},gender={self.gender},address={self.address},email={self.email},phone={self.phone})"
