import uvicorn
from enum import Enum
from fastapi import FastAPI, Response, status


class op_name(str, Enum):
    sum = "suma"
    sub = "odejmowanie"
    multi = "mnozenie"
    div = "dzielenie"
    power = "potegowanie"
    root = "pierwiastek"


app = FastAPI()


@app.post("/calculator", status_code=200)
def calculator(operation: op_name, x: int, y: int, response: Response):
    if operation == operation.sum:
        return x + y

    elif operation == operation.sub:
        return x - y

    elif operation == operation.multi:
        return x * y

    elif operation == operation.div:
        if y != 0:
            return x / y
        else:
            response.status_code = 400
            return "Error: dividing by 0 is prohibited"

    elif operation == operation.power:
        return pow(x, y)

    elif operation == operation.root:
        if y > 1 and x > 0:
            return x ** (1 / float(y))
        else:
            response.status_code = 400
            return "Error: y must be > 2 and x > 0 to make root calculation"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
