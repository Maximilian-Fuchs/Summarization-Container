from flask import Flask, url_for, json, request
app = Flask(__name__)
from pyteaser import Summarize, SummarizeUrl

#setup
host = '0.0.0.0'
port = 5001


@app.route('/summarize', methods = ['POST'])
def summarize():
    args = request.json['args']
    article_title = args[0]
    article_text = args[1]
    request.json['result'] = Summarize(article_title, article_text)
    return ' '.join(request.json['result']).encode('utf_8')

if __name__ == '__main__':
    app.run(host=host, port=port)
