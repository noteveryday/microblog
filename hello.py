from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    host = request.headers.get('Host')
    return '<h1> Hello World!</h1><br /><p>Your browser is %s.<br/>Your Host is %s.</p>' % (user_agent,host)

if __name__ == '__main__':
    app.run(debug = True)
# test
