# Employee Management System (Flask)

A full-stack **Employee Management System** built using **Flask**, **SQLAlchemy**, **MySQL**, and **Bootstrap**. The application helps organizations manage employees, departments, attendance, leave requests, and user authentication through a simple and responsive web interface.

---

## Features

### Authentication
- User Registration
- User Login
- Secure Logout
- Password Hashing
- Change Password
- User Profile

### Employee Management
- Add Employee
- View Employees
- Edit Employee
- Delete Employee
- Employee Details

### Department Management
- Add Department
- View Departments
- Delete Department

### Attendance Management
- Employee Check-In
- Employee Check-Out
- Attendance History

### Leave Management
- Apply Leave
- View Leave Requests
- Approve Leave
- Reject Leave

### Dashboard
- Total Employees
- Total Departments
- Total Positions
- Total Leave Requests
- Recent Employees
- Employees by Department Chart
- Leave Status Chart

### Export
- Export Employees to Excel (.xlsx)

---

## Tech Stack

### Backend
- Python
- Flask
- Flask-Login
- Flask-Migrate
- SQLAlchemy

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Jinja2
- Chart.js

### Database
- MySQL

### Tools
- Git
- GitHub
- VS Code

---

## Project Structure

```
employee-management-system-flask/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── __init__.py
│
├── migrations/
├── instance/
├── requirements.txt
├── config.py
├── run.py
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/employee-management-system-flask.git
```

### Navigate to Project

```bash
cd employee-management-system-flask
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Create a MySQL database and update your database connection settings in the project configuration.

### Apply Migrations

```bash
flask db upgrade
```

### Run Application

```bash
python run.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Screenshots

Add screenshots of the following pages:

- Login
- Dashboard
- Employees
- Departments
- Attendance
- Leave Management
- Profile

---

## Future Improvements

- Edit Department
- PDF Export
- Search & Filters
- Pagination
- Email Notifications
- REST API
- Docker Support
- Deployment on Render

---

## Learning Outcomes

This project demonstrates knowledge of:

- Flask Framework
- SQLAlchemy ORM
- CRUD Operations
- Authentication & Authorization
- Database Design
- Bootstrap UI
- Chart.js Integration
- Excel Export
- Git & GitHub
- MVC Architecture

---

## Author

**Om Wable**

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://www.linkedin.com/in/YOUR_LINKEDIN

---

## License

This project is developed for educational and portfolio purposes.
