import os

import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find("div", id="content")
    quote = facts.getText()
    quote = quote.replace(".", "")
    r = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/',
                      allow_redirects=False, data={'input_text': quote})
    return r.headers['Location']


@app.route('/')
def home():
    fact = get_fact()
    return render_template('base.jinja2', fact=fact)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

