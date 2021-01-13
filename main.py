from enum import Enum
from fastapi import FastAPI


class op_name(str, Enum):
    suma = "suma"
    odejmowanie = "odejmowanie"
    mnozenie = "mnozenie"
    dzielenie = "dzielenie"
    potegowanie = "potegowanie"
    pierwistek = "pierwiastek"


app = FastAPI()


@app.get("/calculator")
def calculator(operacja: op_name, x: int, y: int):
    if operacja == operacja.suma:
        return x + y

    elif operacja == operacja.odejmowanie:
        return x - y

    elif operacja == operacja.mnozenie:
        return x * y

    elif operacja == operacja.dzielenie:
        if y != 0:
            return x / y
        else:
            return "Nie dziel cholero nigdy przez zero"

    elif operacja == operacja.potegowanie:
        return pow(x, y)

    elif operacja == operacja.pierwistek:
        return x ** (1 / float(y))
