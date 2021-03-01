from flask import Flask

app = Flask(__name__)


@app.route('/test_apikey', methods=['GET'])
def get():
    return 'Hello api Key', 200


@app.route('/test_jwt', methods=['GET'])
def get2():
    return 'Hello JWT', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
