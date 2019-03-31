from flask_restful import Resource, Api, reqparse
import spacy
import en_core_web_sm
from resources.html_document import HtmlDocument


class FindKeywords(Resource):
  def get(self):

    # This API needs a url argument
    parser = reqparse.RequestParser()
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    
    # This is the URL that we want to extract the keywords from
    url = args["url"]
    
    htmlDocument = HtmlDocument(url)

    text = htmlDocument.getBody()

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    ret = {}

    for entity in doc.ents:
        ret[entity.text] = entity.label_ 

    return ret, 200
    