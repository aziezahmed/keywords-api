from flask_restful import Resource, Api, reqparse
import requests
from bs4 import BeautifulSoup
import spacy
import en_core_web_sm

class FindKeywords(Resource):
  def get(self):
    
    ret = {}

    # This API needs a url argument
    parser = reqparse.RequestParser()
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    
    # This is the URL that we want to extract the keywords from
    url = args["url"]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    ret["title"] = soup.title.text 
    
    header_concat = ""
    headers = []
    for header in soup.find_all('h1'):
        headers.append(header.text)
        header_concat = header_concat + header.text + " "
    ret["headers"]= headers

    paragraphs = []
    paragraph_concat = ""
    for paragraph in soup.find_all('p'):
        if len(paragraph.text.split()) > 5:
            paragraphs.append(paragraph.text)
            paragraph_concat = paragraph_concat + paragraph.text + " "

    ret["paragraphs"]= paragraphs

    text = soup.title.text 
    # Load English tokenizer, tagger, parser, NER and word vectors
   
    nlp = spacy.load('en_core_web_sm')

    title_entities = []
    header_entities = []
    paragraph_entities = []

    # TITLE
    doc = nlp(text.encode('utf8').decode("utf-8"))
    for entity in doc.ents:
        if entity.label_ is "ORG" or entity.label_ is "GPE":
            title_entities.append(entity.text)

    # HEADERS
    text = header_concat
    doc = nlp(text.encode('utf8').decode("utf-8"))
    for entity in doc.ents:
        if entity.label_ is "ORG" or entity.label_ is "GPE":
            header_entities.append(entity.text)

    # PARAGRAPHS
    text = paragraph_concat
    doc = nlp(text.encode('utf8').decode("utf-8"))
    for entity in doc.ents:
        #if entity.label_ is "ORG" or entity.label_ is "GPE"  or entity.label_ is "PERSON":
        paragraph_entities.append(entity.text)

    ret["paragraph_entities"] = paragraph_entities
    ret["header_entities"] = header_entities
    ret["title_entities"] = title_entities

    return ret, 200
    