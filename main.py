from fastapi import FastAPI
from models.user import User

app = FastAPI()

@app.get("/")
async def root():
	return {
		"message": "Hi FastAPI!"
	}

@app.get("/users")
async def users():
	user1 = User(name="Irving", last_name="Juárez", age=21, website="https://irvingvjuarez.com")

	return [
		user1
	]

@app.get("/users/{user_id}")
async def user_detail(user_id):
	return f"Hello {user_id}"