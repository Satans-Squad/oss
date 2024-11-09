from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Make sure the Flask app listens on 0.0.0.0 and the correct port (5000)
    app.run(host='0.0.0.0', port=5000)
