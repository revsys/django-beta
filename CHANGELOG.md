# Changelog

## Version 0.3.0

_Released October 13th, 2026_

- Officially support Python 3.15, including the free-threaded build (3.15t),
  now that 3.15.0 final has been released (#6)
- Drop support for Python 3.10, which has reached end of life. Python 3.11 is
  now the minimum supported version (#7)

## Version 0.2.1

_Released August 1st, 2026_

- Test against Python 3.15, including the free-threaded build (3.15t). It was
  still in beta, so the trove classifier was published but support was not
  promised until the final release (#5)
- Add PyPI, Python, and Django version badges to the README

## Version 0.2.0

_Released July 30th, 2026_

- Modernize packaging and tooling: move to `pyproject.toml` with the hatchling
  build backend, nox, just, prek, and ruff (#3)
- Add support for Django 4.2 through 6.1 and Python 3.10 through 3.14,
  including free-threaded 3.14
- Modernize `beta` for current Django: `path()`, `django.urls.reverse`,
  `get_queryset`, `__str__`, and `AppConfig`-based signal wiring
- Add an initial migration for `BetaSignup`
- Add a test project and pytest-django test suite
- Remove the `.defaults` Django URL imports (#1)

## Earlier releases

This project had no changelog before 0.2.0. Version 0.1.0 was released to PyPI
on September 14th, 2011. See the
[commit history](https://github.com/revsys/django-beta/commits/main) for details.
