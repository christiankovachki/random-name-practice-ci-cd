from random import choice, randint

from faker import Faker
from models.user import User, Title, Country
from settings import settings


class UserFactory:
    def __init__(self):
        self.fake = Faker()

    def _generate_names_based_on_title(self):
        title = choice([Title.MR.value, Title.MRS.value])

        match title:
            case "Mr.":
                first_name = self.fake.first_name_male()
                last_name = self.fake.last_name_male()
            case "Mrs.":
                first_name = self.fake.first_name_female()
                last_name = self.fake.last_name_female()
            case _:
                first_name = self.fake.first_name()
                last_name = self.fake.last_name()

        return title, first_name, last_name

    def _generate_username_based_on_first_name(self, first_name: str):
        name = first_name.lower().replace("'", "").replace(" ", "")
        separator = choice([".", "_", "-"])

        return f"{name}{separator}{randint(10, 9999)}"

    def _generate_email_based_on_username(self, username: str):
        second_level_domain = choice(["example", "testmail", "mailtest"])
        top_level_domain = choice(["com", "net", "org"])

        return f"{username}@{second_level_domain}.{top_level_domain}"

    def _get_country_city(self, country) -> str:
        cities = {
            "India": ["Mumbai", "Delhi", "Bangalore", "Hyderabad"],
            "United States": ["New York", "Los Angeles", "Chicago", "Houston"],
            "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary"],
            "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
            "Israel": ["Jerusalem", "Tel Aviv", "Haifa", "Beersheba"],
            "New Zealand": ["Auckland", "Wellington", "Christchurch", "Hamilton"],
            "Singapore": ["Tampines", "Bedok", "Woodlands", "Sengkang"]
        }
        return choice(cities.get(country))

    def _generate_geo_data(self):
        country = choice(list(Country)).value

        return {
            "country": country,
            "address": f"{country} Address {self.fake.building_number()}",
            "second_address": f"{country} 2nd Address {self.fake.building_number()}",
            "state": f"{country} State {self.fake.postalcode_in_state()}",
            "city": self._get_country_city(country)
        }

    def create_user(self):
        title, first_name, last_name = self._generate_names_based_on_title()
        username = self._generate_username_based_on_first_name(first_name)
        email = self._generate_email_based_on_username(username)
        geo_data = self._generate_geo_data()

        user = User(
            title=title,
            username=username,
            email=email,
            password=self.fake.password(length=12, special_chars=True, digits=True),
            day_of_birth=self.fake.day_of_month().lstrip("0"),
            month_of_birth=self.fake.month_name(),
            year_of_birth=str(self.fake.date_of_birth(minimum_age=18, maximum_age=65).year),
            first_name=first_name,
            last_name=last_name,
            company=self.fake.company(),
            address=geo_data.get("address"),
            second_address=geo_data.get("second_address"),
            country=geo_data.get("country"),
            state=geo_data.get("state"),
            city=geo_data.get("city"),
            zipcode=self.fake.zipcode(),
            mobile_number=self.fake.msisdn()
        )

        return user

    @staticmethod
    def get_existing_user_username() -> str:
        return settings.TEST_USER_USERNAME

    @staticmethod
    def get_existing_user_email() -> str:
        return settings.TEST_USER_EMAIL
