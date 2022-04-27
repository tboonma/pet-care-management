from venv import create
from requests import session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.pet_dao import PetDao
from utils.dao.customer_dao import CustomerDao


class PetCare:

    def __init__(self, connection_url="sqlite:///sample.db") -> None:
        engine = create_engine(connection_url)
        session = sessionmaker(bind=engine)
        self.__db_session = session()

    def pet(self):
        return PetDao(self.__db_session)

    def customer(self):
        return CustomerDao(self.__db_session)
