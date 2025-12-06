from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/search")
def search_items(
    keyword: str,
    limit: int = Query(..., ge=1, le=100)
):
    return {
        "keyword": keyword,
        "limit": limit,
        "message": f"Searching for '{keyword}' with a limit of {limit} results."
    }
