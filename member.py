class Member():
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


class Address():

    def setStreetName(streetName) -> None:
        self.streetName: str = streetName

    def setHouseNumber(houseNumber) -> None:
        self.houseNumber: int = houseNumber

    def setZipCode(zipCode) -> None:
        self.zipCode: str = zipCode

    def setCity(city) -> None:
        self.city: str = city
