from utils.petcare import PetCare
from models.customer_model import CustomerModel
from models.pet_model import PetModel

pet_care = PetCare()

# print(pet_care.customer().get_all_customers())
# print(pet_care.customer().get_customer_info_by_id(2))
# print(pet_care.customer().get_customer_by_firstname("Evie"))
# print(pet_care.pet().get_all_pets())
# print(pet_care.pet().get_pet_info_by_id(2))
# print(pet_care.pet().get_pet_by_name("Marvin"))
# print(pet_care.pet().get_pet_by_owner_id(68))
# print(pet_care.pet().get_pet_by_type("cat"))

# new_customer = CustomerModel(firstName="Tawan", lastName="Boonma", gender="Male", address="Bangkok", email="tawan.boo@ku.th", phoneNumber="191")
# pet_care.customer().add_new_customer(new_customer)
# print(pet_care.customer().get_customer_by_firstname("Tawan"))

# new_pet = PetModel(name="FooFoo", type="Scottish Fold cat", gender="Female", birthyear=2019, owner_id=81)
# pet_care.pet().add_new_pet(new_pet)
print(pet_care.pet().get_pet_by_name("FooFoo"))