from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    method = request.method
    url = request.url
    
    print(f"🛑 Incoming Request → {method} {url}")
    
    response = await call_next(request)
    return response

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}
