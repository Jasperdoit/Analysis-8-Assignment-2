from datetime import datetime

class Member():
    def __init__(self, password : str, firstName : str, lastName : str, registrationDate : datetime = datetime.now()):
        self.username : str = username
        self.password : str = password
        self.firstName : str = firstName
        self.lastName : str = lastName
        self.registrationDate : datetime = registrationDate



    # self.firstName = ""
    # self.lastName = ""
    # self.age = 0
    # self.gender = ""
    # self.weight = ""
    # self.email = ""
    # self.phone = ""

    def setFirstName(firstname: str) -> None:
        self.firstName: str = firstname

    def setLastName(lastname: str) -> None:
        self.lastName: str = lastname

    def setAge(age: int) -> None:
        if (age < 16):
            return "error"
        self.age: int = age

    def setGender(gender: str) -> str:
        if gender != "M" and gender != "F":
            return "error"
        self.gender: str = gender
        return "sucess"

    def setWeight(weight: str) -> None:
        self.weight: str = weight

    def setEmail(email: str) -> None:
        self.email: str = email

    def setPhone(phone: str) -> None:
        self.phone: str = phone


    def to_tuple(self):
        return (self.username, self.password, self.firstName, self.lastName, self.registrationDate, self.role)

    def from_tuple(tuple) -> 'Member':
        Member = Trainer(tuple[1], tuple[2], tuple[3], tuple[4], tuple[5])
        trainer.id = tuple[0]
        return trainer


class Address():

    def setStreetName(streetName) -> None:
        self.streetName: str = streetName

    def setHouseNumber(houseNumber) -> None:
        self.houseNumber: int = houseNumber

    def setZipCode(zipCode) -> None:
        self.zipCode: str = zipCode

    def setCity(city) -> None:
        self.city: str = city
