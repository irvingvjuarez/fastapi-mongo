from fastapi import FastAPI
from models.user import User
from db.data import users_data

app = FastAPI()

@app.get("/")
async def root():
	return {
		"message": "Hi FastAPI!"
	}

@app.get("/users")
async def users(skip: int = 0, limit: int = len(users_data)):
	return users_data[skip:skip + limit]

@app.get("/users/{user_id}")
async def user_detail(user_id: int):
	try:
		user = list( filter(lambda item: dict(item)["id"] == user_id, users_data) )

		if len(user) >= 1:
			return user
		else:
			raise Exception(f"Item with id {user_id} not found")
	except:
		raise Exception(f"Item with id {user_id} not found")