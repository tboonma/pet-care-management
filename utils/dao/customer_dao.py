from models.customer_model import CustomerModel
from sqlalchemy.orm.session import Session


class CustomerDao:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_all_customers(self):
        return self.__session.query(CustomerModel).all()

    def get_customer_info_by_id(self, id):
        return self.__session.query(CustomerModel).filter(CustomerModel.id == id)[0]

    def get_customer_by_firstname(self, firstname):
        return self.__session.query(CustomerModel).filter(CustomerModel.firstName == firstname).all()

    def add_new_customer(self, customer: CustomerModel):
        self.__session.add(customer)
        self.__session.commit()
        print(
            f"Added customer:'{customer.firstName} {customer.lastName}' to the database")
