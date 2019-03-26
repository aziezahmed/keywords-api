from flask import Flask
from flask_restful import Api

from resources.find_symbols import FindSymbols

app = Flask(__name__)
api = Api(app)

api.add_resource(FindSymbols, "/find_symbols/")

if __name__ == "__main__":
  app.run()