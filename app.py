# required imports
from flask import Flask

# instantiate the application object
app = Flask(__name__)

# create an endpoint with a decorator
@app.route("/")
def hello():
  return "Hello World"

if __name__ == "__main__":
  app.run()
