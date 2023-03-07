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
async def users():

	return users_data

@app.get("/users/{user_id}")
async def user_detail(user_id):
	return f"Hello {user_id}"