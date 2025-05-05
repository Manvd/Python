from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)

# HTML template with Bootstrap
TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Management System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">
    <h1 class="text-center mb-4">📚 Student Management System</h1>
    
    <div class="card p-4 shadow-sm mb-4">
        <h4>Add New Student</h4>
        <form method="POST" action="/add" class="row g-3">
            <div class="col-md-4">
                <input type="text" name="name" class="form-control" placeholder="Name" required>
            </div>
            <div class="col-md-4">
                <input type="number" name="age" class="form-control" placeholder="Age" required>
            </div>
            <div class="col-md-4">
                <input type="text" name="grade" class="form-control" placeholder="Grade" required>
            </div>
            <div class="col-12">
                <button type="submit" class="btn btn-primary">Add Student</button>
            </div>
        </form>
    </div>

    <div class="card p-4 shadow-sm">
        <h4>Student Records</h4>
        {% if students %}
        <table class="table table-bordered table-striped mt-3">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Grade</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% for student in students %}
                <tr>
                    <td>{{ student[0] }}</td>
                    <td>{{ student[1] }}</td>
                    <td>{{ student[2] }}</td>
                    <td>{{ student[3] }}</td>
                    <td>
                        <a href="/delete/{{ student[0] }}" class="btn btn-sm btn-danger">Delete</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p class="text-muted">No students added yet.</p>
        {% endif %}
    </div>
</div>
</body>
</html>
'''

# Database setup
def init_db():
    conn = sqlite3.connect("students_flask.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET"])
def index():
    conn = sqlite3.connect("students_flask.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template_string(TEMPLATE, students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    age = request.form["age"]
    grade = request.form["grade"]
    conn = sqlite3.connect("students_flask.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_student(id):
    conn = sqlite3.connect("students_flask.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
