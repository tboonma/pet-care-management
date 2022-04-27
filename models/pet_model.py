from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PetModel(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    birthyear = Column(Text, nullable=False)
    owner_id = Column(Text)

    def __repr__(self) -> str:
        return f"<Pet: (id={self.id},name={self.name},type={self.type},gender={self.gender},birth_year={self.birthyear},owner_id={self.owner_id})>"
