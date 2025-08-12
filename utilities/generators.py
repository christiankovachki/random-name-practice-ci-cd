from random import randint
from faker import Faker


class Generators:
    _fake = Faker()

    @classmethod
    def generate_random_int(cls, min_int: int = 100, max_int: int = 999999) -> int:
        return randint(min_int, max_int)

    @classmethod
    def generate_random_subject(cls):
        order_number = cls.generate_random_int()
        return f"Question about order #{order_number}"

    @classmethod
    def generate_random_text(cls, max_chars = 500):
        return cls._fake.text(max_nb_chars=max_chars)

    @classmethod
    def generate_payment_card_details(cls):
        credit_card_number = cls._fake.credit_card_number()
        credit_card_cvc = cls._fake.credit_card_security_code()
        credit_card_expiration_date = cls._fake.credit_card_expire(date_format="%m/%Y").split("/")
        credit_card_expiration_month = credit_card_expiration_date[0]
        credit_card_expiration_year = credit_card_expiration_date[1]

        return {
            "card_number": credit_card_number,
            "card_cvc": credit_card_cvc,
            "card_expiration_month": credit_card_expiration_month,
            "card_expiration_year": credit_card_expiration_year
        }
