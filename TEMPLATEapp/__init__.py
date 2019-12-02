# the sole purpose of this script is to initialize the app on first start or restart

# importing the Flask object from the dependancy
from flask import Flask

# instantiate the central object. Variable name "app" is what pilot script seeks
app = Flask(__name__)

# import the routes module from the main folder of the app
from TEMPLATEapp import routes
