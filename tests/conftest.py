"""
Pytest configuration and fixtures for testing the FastAPI application.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities data before each test."""
    # Store original state
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Join the school basketball team and compete in league games",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 15,
            "participants": ["james@mergington.edu", "liam@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Improve swimming technique and participate in swim meets",
            "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["ava@mergington.edu", "noah@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore various art mediums including painting, drawing, and sculpture",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["mia@mergington.edu", "isabella@mergington.edu"]
        },
        "Drama Club": {
            "description": "Develop acting skills and perform in school theater productions",
            "schedule": "Wednesdays and Fridays, 3:30 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["ethan@mergington.edu", "charlotte@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop critical thinking and public speaking through competitive debate",
            "schedule": "Mondays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["william@mergington.edu", "amelia@mergington.edu"]
        },
        "Science Olympiad": {
            "description": "Compete in science competitions and conduct research projects",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["benjamin@mergington.edu", "harper@mergington.edu"]
        }
    }
    
    # Reset activities to original state
    activities.clear()
    activities.update(original_activities)
    
    yield
    
    # Clean up after test
    activities.clear()
    activities.update(original_activities)
