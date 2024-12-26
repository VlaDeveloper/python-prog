import json
from fastapi import FastAPI

app = FastAPI()

f = open("csvjson.json", "r", encoding="utf8")
r = f.read()
y = json.loads(r)

@app.get("/games")
async def get_metrics():
    return {"games": y}