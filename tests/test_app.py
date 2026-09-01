from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)
original_activities = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(deepcopy(original_activities))
    yield
    activities.clear()
    activities.update(deepcopy(original_activities))


def test_root_redirects_to_static_interface():
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_seeded_activity_data():
    response = client.get("/activities")

    assert response.status_code == 200
    activities_response = response.json()
    assert len(activities_response) == 9
    assert activities_response["Chess Club"] == {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    }


def test_signup_adds_student_to_activity():
    email = "student@mergington.edu"

    response = client.post(f"/activities/Chess%20Club/signup?email={email}")

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}
    assert email in client.get("/activities").json()["Chess Club"]["participants"]


def test_signup_rejects_unknown_activity():
    response = client.post("/activities/Unknown%20Club/signup?email=student@mergington.edu")

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_rejects_duplicate_student():
    response = client.post(
        "/activities/Chess%20Club/signup?email=michael@mergington.edu"
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Student already signed up for this activity"
    }


def test_unregister_removes_student_from_activity():
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/Chess%20Club/participants/{email}")

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from Chess Club"}
    assert email not in client.get("/activities").json()["Chess Club"]["participants"]


def test_unregister_rejects_unknown_activity():
    response = client.delete(
        "/activities/Unknown%20Club/participants/student@mergington.edu"
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_rejects_student_not_signed_up_for_activity():
    response = client.delete(
        "/activities/Chess%20Club/participants/student@mergington.edu"
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Student is not signed up for this activity"
    }