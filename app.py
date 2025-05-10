from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # This allows all domains to access your API

@app.route('/todos/1')
def get_todo():
    return jsonify({
        "userId": 1,
        "id": 1,
        "title": "Sample Todo"
    })

if __name__ == '__main__':
    app.run()
