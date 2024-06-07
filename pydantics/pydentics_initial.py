from typing import Optional
from pydantic import BaseModel, Field, AliasChoices, AliasPath, computed_field


class Address(BaseModel):
    class Config:
        underscore_attrs_are_private = True
    
    street_name: str = Field(validation_alias=AliasPath("nesting1", "nesting2"))
    house_number: int = Field(validation_alias=AliasPath("house_number"))
    ffull_address : int = Field(validation_alias=AliasPath("house_number"), exclude=True)

    @computed_field(return_type=list)
    def full_address(self):
        return [f"{self.house_number} {self.street_name}"]
    
    @computed_field(alias = "house_number", return_type=list)
    def full_address2(self):
        return [f"{self.house_number} {self.street_name}"]

class Owner(BaseModel):
    name: str = Field(validation_alias=AliasChoices("full_name", "owner_name"))
    age: int = Field(validation_alias=AliasChoices("yob"))
    address: list[Address] = Field(validation_alias=AliasPath("address"))

    @computed_field(return_type=dict)
    def model(self):
        return AliasPath("address").convert_to_aliases(self.dict())

    
def main():
    # owner = Owner(name="Abhijeet", age="123", address="803i")
    # car = Car(name="BMW", model="X1", year=2021, owner=owner)
    # print(car.model_dump_json())
    internal ={"full_name": "Abhijeet", 
                                  "yob" : 2024, 
                                  "address" :[{
                                        "street_name": "ABC",
                                        "house_number": 123,
                                        "nesting1": {
                                            "nesting2" : "success"
                                        }
                                  }], 
                                  "occupation" : "IT"}
    owner = Owner.model_validate(internal)
    print(owner.model_dump())

    print("nesting2" in internal)
    
if __name__=="__main__":
    main()