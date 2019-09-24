import pytest

from test_project.users.models import User

@pytest.mark.django_db
def test_orm_access():
    assert User.objects.all()
