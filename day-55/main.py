from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route('/')
@make_bold
@makeitalic
@make_underline
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)