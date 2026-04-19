from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}
next_id = 1

# Home route (to avoid confusion)
@app.route('/')
def home():
    return "Flask is running! Use /students"

# GET all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values()))

# POST add student
@app.route('/students', methods=['POST'])
def add_student():
    global next_id
    data = request.get_json()

    student = {
        "id": next_id,
        "name": data["name"],
        "roll": data["roll"]
    }

    students[next_id] = student
    next_id += 1

    return jsonify(student), 201

# DELETE student
@app.route('/students/<int:sid>', methods=['DELETE'])
def delete_student(sid):
    students.pop(sid, None)
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(debug=True)