# FastAPI allows you to declare additional information and validation for your parameters.

from typing import Optional, List
from fastapi import FastAPI, Query

app = FastAPI()

# Validation
## We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Query parameter list / multiple values
@app.get("/items/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


# Declare more metadata
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Alias Parameters
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Deprecating parameters
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Exclude from OpenAPI
@app.get("/items/")
async def read_items(
    hidden_query: Optional[str] = Query(None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
