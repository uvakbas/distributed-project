from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "CS 550 Project..."
    
@app.route('/test',methods = ['POST'])
def test_post():
   return "Data Received"  + json.dumps(request.get_json())

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
