from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return "Hello, World!"


@app.get("/users/me")
def get_current_user():
    return {"user_id": 123}


# no type hint
# @app.get("/users/{user_id}")
# def get_user(user_id):
#     return {"user_id": user_id}


# type hint
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
