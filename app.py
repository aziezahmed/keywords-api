from flask import Flask
from flask_restful import Api

from resources.find_keywords import FindKeywords

app = Flask(__name__)
api = Api(app)

api.add_resource(FindKeywords, "/find_keywords/")

if __name__ == "__main__":
  app.run()