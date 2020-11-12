import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

template = """

"""


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_link(fact):
    payload = {'input_text': fact}
    url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'

    r = requests.post(url, data=payload)

    return r.url


@app.route('/')
def home():
    fact = get_fact().strip()
    link = get_link(fact)
    body = '<a href="{}">{}</a>'.format(link,link)

    return Response(response=body, mimetype="text/html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

