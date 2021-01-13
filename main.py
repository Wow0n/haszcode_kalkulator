from enum import Enum
from fastapi import FastAPI


class op_name(str, Enum):
    sum = "suma"
    sub = "odejmowanie"
    multi = "mnozenie"
    div = "dzielenie"
    power = "potegowanie"
    root = "pierwiastek"


app = FastAPI()


@app.get("/calculator")
def calculator(operation: op_name, x: int, y: int):
    if operation == operation.sum:
        return x + y

    elif operation == operation.subtraction:
        return x - y

    elif operation == operation.multi:
        return x * y

    elif operation == operation.div:
        if y != 0:
            return x / y
        else:
            return "Nie dziel cholero nigdy przez zero"

    elif operation == operation.power:
        return pow(x, y)

    elif operation == operation.root:
        return x ** (1 / float(y))
