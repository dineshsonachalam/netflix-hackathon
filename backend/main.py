import json
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crud import get_battle_statistics, execute_sql_file

app = FastAPI()
execute_sql_file()

origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/battles")
def read_item():
    battle_info = json.loads(get_battle_statistics())
    return battle_info

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)



