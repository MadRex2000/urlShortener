import json
import flask
from flask import request, redirect, abort


app = flask.Flask(__name__)


def link(ln):
    files = open('link.json', 'r')
    links = json.load(files)
    url = links[ln]
    files.close()
    return redirect(url, code=302)


@app.route('/ls')
def links():
    files = open('link.json', 'r')
    links = json.load(files)
    files.close()
    return links


def upload(ln, target):
    files = open('link.json', 'r')
    links = json.load(files)
    links[ln] = target
    links = json.dumps(links)
    files.close()
    files = open('link.json', 'w')
    files.write(links)
    files.close()
    return 'OK'


@app.route('/<string:ln>')
def api(ln):
    try:
        target = request.args.get('url')
        if target:
            return upload(ln, target)
        else:
            return link(ln)
    except:
        abort(404)


def run():
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    run()
