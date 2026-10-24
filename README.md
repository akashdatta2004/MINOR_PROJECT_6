# Student Registration System — Flask Mini Project

## 1. Project overview
This is a beginner-friendly web application built with Python Flask. It collects student name, roll number, course, and email, validates the input, and displays a registration confirmation.

## 2. Requirements
- Python 3.9 or later
- pip
- A web browser

## 3. Folder structure
```text
student_registration_flask_project/
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── about.html
│   └── students.html
└── static/
    └── style.css
```

## 4. Run the application
Open a terminal in this project folder.

### Windows
```bash
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open the local address printed in the terminal, usually `http://127.0.0.1:5000`.

## 5. Routes
| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Displays the registration form |
| `/about` | GET | Displays project information |
| `/register` | POST | Validates form data and displays the result |
| `/students` | GET | Lists registrations stored during this server session |

## 6. Validation
- Name cannot be blank and must have at least two characters.
- Roll number cannot be blank.
- Course cannot be blank.
- Email must contain `@` and a domain suffix separated by a dot.
- Errors are shown in a friendly message on the result page.

## 7. Testing checklist
1. Start the application and confirm that the home page loads.
2. Submit all valid fields and confirm the success message and details.
3. Submit the form with blank fields (remove `required` in browser developer tools or send a direct POST) and confirm validation errors.
4. Enter an invalid email and confirm an error is displayed.
5. Open `/about` and `/students` and confirm both routes load.
6. Register two students and confirm both appear on `/students`.

## 8. Limitations
This learning version uses an in-memory Python list rather than a database. Registrations are cleared when the application restarts. It is intended for local classroom demonstration, not production use.

## 9. Screenshots
After running the app, capture screenshots of:
- Home / registration form
- Successful registration result
- Validation error result
- Registered students page
- About page
