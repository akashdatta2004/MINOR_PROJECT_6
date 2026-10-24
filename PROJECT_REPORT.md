# Flask Mini Project Report
## Student Registration System

### 1. Introduction
The Student Registration System is a simple web application developed using Python and the Flask framework. It provides a form for entering student details and returns a clear message after validating the submitted information.

### 2. Objective
The objective is to practise Flask routes, HTML templates, GET and POST requests, form handling, basic validation, and displaying a meaningful result.

### 3. Problem statement
Manual collection of student details can be repetitive. This mini application demonstrates a basic digital form through which a user can enter a student's name, roll number, course, and email address.

### 4. Tools and technologies
- Python
- Flask
- HTML
- CSS
- Jinja template syntax

### 5. Application design
- **Home (`/`)**: shows the student registration form.
- **About (`/about`)**: explains the project and learning objectives.
- **Register (`/register`, POST)**: receives the submitted form, checks the fields, and displays either errors or a successful registration result.
- **Students (`/students`)**: displays student records stored during the current running session.

### 6. Input validation
The application checks that the name, roll number, course, and email are not blank. It also checks that the name has at least two characters and that the email has a basic email-like format. If validation fails, a friendly error message is displayed.

### 7. Expected output
For valid input, the result page displays a success message and the entered student details. For invalid input, the page lists the fields that need correction. The student list page displays registrations entered during the current server session.

### 8. Testing plan
| Test | Input | Expected result |
|---|---|---|
| Valid registration | All fields correctly filled | Success message and student details |
| Empty name | Name left blank | Validation error |
| Short name | One character | Validation error |
| Missing roll number | Roll number blank | Validation error |
| Missing course | Course blank | Validation error |
| Invalid email | Email without a valid basic format | Validation error |
| Open About | Visit `/about` | About page loads |
| Open student list | Visit `/students` | List or empty-state message appears |

### 9. Limitations
Student details are held in memory and are not saved permanently. Data is cleared when the server restarts. The application does not include login, database storage, or deployment because these are optional for the supplied beginner-level brief.

### 10. Conclusion
This project demonstrates the core concepts required for a basic Flask application: routes, HTML templates, form submission, input validation, and meaningful output. It can be extended later with database storage and additional features.
