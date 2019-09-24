import pytest

from test_project.users.models import User

@pytest.mark.django_db
def test_annotate_one():
    assert User.objects.all()
