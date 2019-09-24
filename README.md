# Test Project

I can't get pytest-django to access the data that is in the Postgres. Reproduction steps:

```shell
# Test requirements included, run in a virtualenv
$ make install

# Run all services (Django + Postgres)
$ make run

# Populate the Postgres with a User
$ make populate_postgres

# Run a test to check for that User with DATABASE_URL=postgres://postgresuser:mysecretpass@localhost:5432/test_project
$ make test
# AssertionError: assert <QuerySet []>
```

However, I can manually check that the data is properly in the Postgres by running the manage.py shell inside of the Django container.
```shell
# DATABASE_URL=postgres://postgresuser:mysecretpass@postgres:5432/test_project
$ sudo docker exec -i test_project_django_1 python3 manage.py shell
Python 3.6.9 (default, Jul 13 2019, 15:16:41) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from test_project.users.models import User

In [2]: User.objects.all()
Out[2]: <QuerySet [<User: cats>]>
```
