from flask import Flask  # Import flask

app = Flask(__name__)  # Setup the flask app by creating an instance of Flask


# When someone goes to / on the server, execute the following function
@app.route('/')
def home():
    return 'Hello, World!'  # Return this message back to the browser


# If the script that was run is this script (we have not been imported)
if __name__ == '__main__':
    app.run()  # Start the server
