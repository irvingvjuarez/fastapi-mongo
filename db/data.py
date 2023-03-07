import sys
sys.path.append("../models")

from models.user import User
from faker import Faker
from random import randint

fake = Faker()

users_data = [
	User(
		id=fake.unique.random_int(),
		name=fake.first_name(),
		last_name=fake.last_name(),
		age=randint(20, 70)
	) for _ in range(10)
]
