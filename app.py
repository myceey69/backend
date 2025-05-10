from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/todos/1', methods=['GET'])
def get_todo():
    todo = {
        "userId": 1423423432,
        "id": 1123,
        "title": "delectus aut autem",
        "completed": False
    }
    return jsonify(todo)

if __name__ == '__main__':
    app.run(debug=True)