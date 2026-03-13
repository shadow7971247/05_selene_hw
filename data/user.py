from dataclasses import dataclass
from typing import List


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: str
    hobbies: List[str]
    picture: str
    address: str
    state: str
    city: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def hobbies_str(self):
        return ", ".join(self.hobbies)

    @property
    def state_city(self):
        return f"{self.state} {self.city}"