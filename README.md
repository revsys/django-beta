# django-beta

`django-beta` is a simple application to help you capture pre-beta interest
with your sites.

By default `django-beta` only captures a user's email address, however you
can alternately set one of these two configuration options:

- `BETA_CAPTURE_FIRST = True` will use a form and require the user to enter
  their first name and email address.
- `BETA_CAPTURE_BOTH = True` will use a form and require the user to enter
  their first name, last name, and email address.

## Installation

Add `beta` to your `INSTALLED_APPS` and run migrations.

Add the following to your `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    path("beta/", include("beta.urls")),
]
```

Using the example templates provided in the code, create your customized beta
signup templates.

## Managers

The `BetaSignup` model has the following manager methods to help out:

```python
BetaSignup.objects.contacted()
BetaSignup.objects.not_contacted()
BetaSignup.objects.registered()
BetaSignup.objects.not_registered()
```

## Side Effects

`django-beta` listens for a signal on User creation and marks the
corresponding `BetaSignup` entry as `registered`.

## Development

This project uses [nox](https://nox.thea.codes/) and
[just](https://github.com/casey/just) for testing and linting across a matrix
of Python and Django versions.

```shell
just lint          # run pre-commit / ruff via prek
just test          # run the full nox test matrix
just test-latest   # run against the latest Python and Django
```

## TODO

- Admin views to show beta registrations over time
- Management commands to simplify emailing the interested users
