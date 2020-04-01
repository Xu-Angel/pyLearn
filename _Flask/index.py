from flask import Flask, escape, request
""" 
https://flask.palletsprojects.com/en/1.1.x/quickstart/
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:

C:\path\to\app>set FLASK_APP=hello.py
And on PowerShell:

PS C:\path\to\app> $env:FLASK_APP = "hello.py"
Alternatively you can use python -m flask:

$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
 """
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'