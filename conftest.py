import pytest
from app import create_app, db


@pytest.fixture
def client():
    app = create_app(testing=True)

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()
