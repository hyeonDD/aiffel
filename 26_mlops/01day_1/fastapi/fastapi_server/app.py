import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}


def start():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start()
