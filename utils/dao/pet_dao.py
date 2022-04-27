from models.pet_model import PetModel
from sqlalchemy.orm.session import Session


class PetDao:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_all_pets(self):
        return self.__session.query(PetModel).all()

    def get_pet_info_by_id(self, id):
        return self.__session.query(PetModel).filter(PetModel.id == id)[0]

    def get_pet_by_name(self, name):
        return self.__session.query(PetModel).filter(PetModel.name == name).all()

    def get_pet_by_owner_id(self, id):
        return self.__session.query(PetModel).filter(PetModel.owner_id == id).all()

    def get_pet_by_type(self, type_name):
        return self.__session.query(PetModel).filter(PetModel.type.contains(type_name)).all()

    def add_new_pet(self, pet: PetModel):
        self.__session.add(pet)
        self.__session.commit()
        print(f"Added pet:'{pet.name}', {pet.type} to the database")