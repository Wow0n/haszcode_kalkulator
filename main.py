import uvicorn
from enum import Enum
from fastapi import FastAPI, Response, status
import mysql.connector


class OpName(str, Enum):
    sum = "suma"
    sub = "odejmowanie"
    multi = "mnozenie"
    div = "dzielenie"
    power = "potegowanie"
    root = "pierwiastek"


app = FastAPI()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fastapi_calculator"
)


def db(result):
    mycursor = mydb.cursor()
    history = ("History of results:", )

    query = ("INSERT INTO history (results) VALUES (%(result)s)")
    data = {'result': result}
    mycursor.execute(query, data)

    mydb.commit()

    mycursor.execute("SELECT results FROM history ORDER BY id DESC")
    myresult = mycursor.fetchall()

    for x in myresult:
        history += x

    return history

    mydb.close()


@app.post("/calculator", status_code=200)
def calculator(operation: OpName, x: int, y: int, response: Response):
    if operation == operation.sum:
        result = x + y
        return result, db(result)


    elif operation == operation.sub:
        result = x - y
        return result, db(result)

    elif operation == operation.multi:
        result = x * y
        return result, db(result)

    elif operation == operation.div:
        if y != 0:
            result = x / y
            return result, db(result)
        else:
            response.status_code = 400
            return "Error: dividing by 0 is prohibited"

    elif operation == operation.power:
        result = pow(x, y)
        return result, db(result)

    elif operation == operation.root:
        if y > 1 and x > 0:
            result = x ** (1 / float(y))
            return result, db(result)
        else:
            response.status_code = 400
            return "Error: y must be > 2 and x > 0 to make root calculation"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
