
from flask import Flask, Request
from flask import Blueprint
from api import api

def create_app():
        app = Flask(__name__)
       

        #api.init_app(app)
        app.register_blueprint(api)
        app.run(debug=True)
        print "create_app"
    
create_app()
