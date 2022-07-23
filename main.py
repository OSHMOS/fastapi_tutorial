from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def get_users(limit: int = 100):
    return {"limit": limit}
