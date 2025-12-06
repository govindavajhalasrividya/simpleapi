from fastapi import FastAPI

app = FastAPI()

# Route 1: Home route (“/”)
@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI!"}

# Route 2: Hello route with a path parameter
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! Great to see you."}

# Route 3: Square route with a number path parameter
@app.get("/square/{num}")
def square_number(num: int):
    return {"number": num, "square": num * num}
