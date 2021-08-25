# from flask import Flask

# app = Flask(__name__)

# @app.route("/greeting")
# def greeting():
#     return {'greeting': 'Hello from Flask! 456'}
    

from guhitApp import app

if __name__ == '__main__':
    app.run(debug=True)