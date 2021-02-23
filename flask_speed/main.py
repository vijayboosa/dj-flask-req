from flask import Flask
import requests

app = Flask(__name__)
url = 'https://google.com'


@app.route('/')
def home():
    response = requests.get(url)
    return {'status_code': response.status_code, 'url': url}

if __name__ == '__main__':
    app.run()