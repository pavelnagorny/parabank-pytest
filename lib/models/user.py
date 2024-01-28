from faker import Faker
from dataclasses import dataclass


@dataclass
class User:
    firstname: str
    lastname: str
    address: str
    city: str
    state: str
    zip_code: str
    phone_number: str
    ssn: str
    username: str
    password: str

    @classmethod
    def generate_random(cls):
        fake = Faker()
        return cls(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            address=fake.address(),
            city=fake.city(),
            state=fake.state(),
            zip_code=fake.zipcode(),
            phone_number=fake.phone_number(),
            ssn=fake.ssn(),
            username=fake.lexify(text='????????????'),
            password="test",
        )
