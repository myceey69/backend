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
          "Believe you can and you're halfway there. —Theodore Roosevelt",
        "The best way to get started is to quit talking and begin doing. —Walt Disney",
        "Don’t let yesterday take up too much of today. —Will Rogers",
        "It always seems impossible until it’s done. —Nelson Mandela",
        "Push yourself, because no one else is going to do it for you.",
        "No pain, no gain. Shut up and train.",
        "Your body can stand almost anything. It’s your mind that you have to convince.",
        "Success starts with self-discipline.",
        "The hardest lift of all is lifting your butt off the couch.",
        "Sore today, strong tomorrow.",
        "Train insane or remain the same.",
        "The only bad workout is the one that didn’t happen.",
        "Work hard in silence, let success make the noise.",
        "You don’t have to be extreme, just consistent.",
        "The pain you feel today will be the strength you feel tomorrow.",
        "A one hour workout is 4% of your day. No excuses.",
        "Discipline is doing what needs to be done, even if you don’t want to do it.",
        "Don’t wish for a good body, work for it.",
        "Wake up. Work out. Look hot. Kick ass.",
        "When you feel like quitting, think about why you started.",
        "Excuses don’t burn calories.",
        "Strength doesn’t come from what you can do. It comes from overcoming what you once thought you couldn’t.",
        "The only bad workout is the one you didn’t do.",
        "The gym is not just a place, it’s a mindset.",
        "Champions are made in the gym."
    ]
    return jsonify({
        "quote": random.choice(quotes)
    })

if __name__ == '__main__':
    app.run()
