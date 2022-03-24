# uvicorn path_parameters:app --reload

# FastAPI는 Starlette를 직접 상속하는 클래스입니다.
from fastapi import FastAPI

app = FastAPI()

# You can declare the type of a path parameter in the function, using standard Python type annotations:
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Order matters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


## Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# Predefined Values
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):  ## Declare a path parameter
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# Path parameters containing paths
@app.get(
    "/files/{file_path:path}"
)  ## In this case, the name of the parameter is file_path, and the last part, :path, tells it that the parameter should match any path.
async def read_file(file_path: str):
    return {"file_path": file_path}
