import pytest
from sqlalchemy.orm import Session

from server.src.app import db
from server.src.users.models import User


@pytest.fixture
def user(session: Session) -> db.Model:
    user = User(email='user@example.com')
    session.add(user)
    session.commit()

    return user


