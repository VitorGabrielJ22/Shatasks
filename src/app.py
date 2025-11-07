from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:index>', methods=['PUT'])
def update_task(index):
    tasks[index] = request.json
    return jsonify(tasks[index])

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    task = tasks.pop(index)
    return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True)
