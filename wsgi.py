from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from bs4 import BeautifulSoup
from tabulate import tabulate

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
            return render_template('index.html')
    
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT",4000))
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=port)
