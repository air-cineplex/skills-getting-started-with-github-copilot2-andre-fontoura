# Mergington High School Activities API

A super simple FastAPI application that allows students to view, sign up for, and unregister from extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities
- Prevent duplicate signups for the same activity
- Unregister students from activities
- Manage participants directly from the web UI

## Getting Started

1. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Run the application from the repository root:

   ```
   python -m uvicorn src.app:app --host 127.0.0.1 --port 8000 --reload
   ```

3. Open your browser and go to:
   - Web interface: http://127.0.0.1:8000/static/index.html
   - API documentation: http://127.0.0.1:8000/docs
   - Alternative documentation: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint                                                            | Description                                                          |
| ------ | ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| GET    | `/activities`                                                       | Get all activities with their details and current participant count  |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu`  | Sign up for an activity (returns 400 for duplicate signup attempts)  |
| DELETE | `/activities/{activity_name}/participants/{email}`                 | Unregister a student from an activity (404 for unknown activity/student) |

## Running Tests

Run all tests:

```bash
pytest
```

Run focused API tests:

```bash
pytest tests/test_app.py -q
```

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:
   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

All data is stored in memory, which means data is reset when the server restarts.
