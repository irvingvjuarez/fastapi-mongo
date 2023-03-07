from pydantic import BaseModel

class User(BaseModel):
	id: float
	name: str
	last_name: str
	age: int