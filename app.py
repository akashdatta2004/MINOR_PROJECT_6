from flask import Flask, render_template, request

app = Flask(__name__)

# Beginner-friendly in-memory storage.
# Records reset whenever the application is restarted.
students = []

@app.route("/")
def index():
    """Display the registration form (GET)."""
    return render_template("index.html")

@app.route("/about")
def about():
    """Explain the purpose of this mini project."""
    return render_template("about.html")

@app.route("/register", methods=["POST"])
def register():
    """Validate submitted student details and show a result (POST)."""
    name = request.form.get("name", "").strip()
    roll_number = request.form.get("roll_number", "").strip()
    course = request.form.get("course", "").strip()
    email = request.form.get("email", "").strip()

    errors = []

    if not name:
        errors.append("Please enter the student's name.")
    elif len(name) < 2:
        errors.append("Name must contain at least 2 characters.")

    if not roll_number:
        errors.append("Please enter a roll number.")

    if not course:
        errors.append("Please select or enter a course.")

    if not email:
        errors.append("Please enter an email address.")
    elif "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        errors.append("Please enter a valid email address.")

    if errors:
        return render_template(
            "result.html",
            success=False,
            errors=errors,
            student=None
        ), 400

    student = {
        "name": name,
        "roll_number": roll_number,
        "course": course,
        "email": email
    }
    students.append(student)

    return render_template(
        "result.html",
        success=True,
        errors=[],
        student=student
    )

@app.route("/students")
def student_list():
    """Display registrations made during this running session (GET)."""
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
