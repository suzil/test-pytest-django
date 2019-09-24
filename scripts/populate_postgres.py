from allauth.account.models import EmailAddress

from test_project.users.models import User

email1 = "cats@kitties.com"
user1 = User.objects.create_user(username="cats", password="123", email=email1)
EmailAddress.objects.update_or_create(
    user=user1, primary=True, defaults=dict(email=email1, verified=True)
)
