from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Step 1: Create Pydantic Model
class User(BaseModel):
    name: str
    email: str
    age: int

# Step 2: Route that accepts the model
@app.post("/create-user")
def create_user(user: User):
    return {
        "message": f"User {user.name} created!",
        "email": user.email.upper(),
        "age_in_5_years": user.age + 5
    }
