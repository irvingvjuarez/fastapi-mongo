from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return {
		"message": "Hi FastAPI!"
	}

@app.get("/users")
async def users():
	return "Hello Users!"

@app.get("/users/{user_id}")
async def user_detail(user_id):
	return f"Hello {user_id}"