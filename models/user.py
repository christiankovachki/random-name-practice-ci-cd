from dataclasses import dataclass
from enum import Enum


class Title(Enum):
    MR = "Mr."
    MRS = "Mrs."


class Country(Enum):
    INDIA = "India"
    UNITED_STATES = "United States"
    CANADA = "Canada"
    AUSTRALIA = "Australia"
    ISRAEL = "Israel"
    NEW_ZEALAND = "New Zealand"
    SINGAPORE = "Singapore"


@dataclass
class User:
    title: str
    username: str
    email: str
    password: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    first_name: str
    last_name: str
    company: str
    address: str
    second_address: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str
