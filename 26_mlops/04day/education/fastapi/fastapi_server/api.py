import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

from fastapi_server.calculator import calculate

app = FastAPI()


@app.get('/')
async def get_root_route():
    return {'message': 'hello modu'}


class Formula(BaseModel):
    x: float
    y: float
    operator: str


@app.post('/calculator')
async def input_formula(input: Formula):
    result = calculate(x=input.x, y=input.y, operator=input.operator)
    return result


def start():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start()
