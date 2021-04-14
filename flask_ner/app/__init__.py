from flask import Flask, render_template, request
import spacy
from spacy import displacy
from spacy.lang.en import English
from .ner_client import NamedEntityClient

app = Flask(__name__)
ner = spacy.load("en_core_web_sm")
ner = NamedEntityClient(ner, displacy)

from app import routes
