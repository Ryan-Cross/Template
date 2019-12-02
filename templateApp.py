# this program is the "pilot" it will initialize the app and set it working

# this call will ask to import the central Flask object named "app"
# it goes to the folder and finds the __init__ and calls it
from TEMPLATEapp import app

# this runs the program as a main versus as a module (ithink...)
if __name__ == '__main__':
    app.run()
