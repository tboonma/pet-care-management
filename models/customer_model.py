from sqlalchemy import Column, Integer, Text, null
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CustomerModel(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(Text, nullable=False)
    lastName = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    phoneNumber = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Customer: (id={self.id},first_name={self.firstName},last_name={self.lastName},gender={self.gender},address={self.address},email={self.email},phone={self.phoneNumber})"
