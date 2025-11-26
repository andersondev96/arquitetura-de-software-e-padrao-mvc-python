from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return {
            PetsTable(name="Fuffly", type="cat", id=4),
            PetsTable(name="Buddy", type="Dog", id=47)
        }

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expect_response = {
        "data": {
                "type": "Pets",
                "count": 2,
                "attributes": [
                    { "name": "Fuffly", "id": 4},
                    { "name": "Buddy", "id": 47}
                ]
            }
    }

    assert response == expect_response
