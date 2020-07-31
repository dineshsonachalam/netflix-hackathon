import json
import uvicorn
from fastapi import FastAPI
from crud import get_battle_statistics

app = FastAPI()


@app.get("/battle_info")
def read_item():
    battle_info = json.loads(get_battle_statistics())
    return battle_info


# http://0.0.0.0:8087/docs
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8087)



