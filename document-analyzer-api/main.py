from flask import Flask, request, abort
from assistants.document_analyst_assistant import DocumentAnalystAssistant
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to the document analyzer using ChatGPT 4!</p>"

@app.route("/document/api/analyze", methods=['POST'])
def analyseDocument():
    data = request.get_json()
    if (data != None):
        prompt = data.get("prompt")
    else: 
        abort(400)
    
    assistant = DocumentAnalystAssistant()
    response = assistant.analyseDocument(prompt, ["../docs/article1.pdf","../docs/article2.txt"])
    
    return response