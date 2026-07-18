# Import Flask - gives us the tools to build a web server
from flask import Flask

# Create the Flask app - this is our actual web application object
app = Flask(__name__)

# The list of car models the company currently has in its fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# @app.route tells Flask: "when someone visits '/', run the function below"
@app.route('/')
def index():
    # Whatever this function returns is what shows up in the browser
    return 'Welcome to Flatiron Cars'

# <model> in the route grabs whatever text is in that part of the URL
# and passes it into the function below as the 'model' argument
@app.route('/<model>')
def get_model(model):
    # Check if the model typed in the URL is in our existing_models list
    if model in existing_models:
        # f-string lets us drop the 'model' variable straight into the text
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'

# Only start the server if this file is run directly (not imported)
if __name__ == '__main__':
    app.run(port=5555, debug=True)