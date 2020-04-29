from fastapi import FastAPI
from controller.readItem import add_postfix

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    result = add_postfix(item_id)
    return {"item_id":result}