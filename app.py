from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Allow all origins

# Route 1: Static todo
@app.route('/todos/1')
def get_todo():
    return jsonify({
        "userId": 1,
        "id": 1,
        "title": "Sample Todo"
    })

# Route 2: Random inspirational quote
@app.route('/inspire')
def get_quote():
    quotes = [
        "Believe you can and you're halfway there. —Theodore Roosevelt",
        "The best way to get started is to quit talking and begin doing. —Walt Disney",
        "Don’t let yesterday take up too much of today. —Will Rogers",
        "It always seems impossible until it’s done. —Nelson Mandela",
        "Push yourself, because no one else is going to do it for you."
    ]
    return jsonify({
        "quote": random.choice(quotes)
    })

if __name__ == '__main__':
    app.run()
