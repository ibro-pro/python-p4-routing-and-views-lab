from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Logs in terminal
    return f'{param}'  # Returns to browser


@app.route('/count/<int:param>')
def count(param):
    numbers = ""
    for i in range(param):
        numbers += f"{i}\n"
    return numbers


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Cannot divide by zero"
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)
