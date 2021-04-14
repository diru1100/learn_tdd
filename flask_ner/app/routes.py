from app import app, ner
from flask import render_template, request
import json


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/ner', methods=['POST'])
def get_named_ents():
    data = request.get_json()
    # response = True
    result = ner.get_ents(data['sentence'])
    response = {"entities": result.get('ents'), "html": result.get('html')}
    return json.dumps(response)


if __name__ == "__main__":
    app.run(debug=True)
