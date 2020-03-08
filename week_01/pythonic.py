a = 1
b = 2
a, b = b, a


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'