from flask import Flask
import os

app = Flask(__name__)

tenant = os.environ['TENANT']

@app.route('/')
def hello():
        return 'strategy service %s' % tenant
