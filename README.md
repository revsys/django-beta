django-beta
===========

``django-beta`` is a simple application to help you capture pre-beta interest
with your sites.

By default ``django-beta`` only captures a user's email address, however you
can alternately set one of these two configuration options:

BETA_CAPTURE_FIRST = True, will use a form and require the user to enter their
first name and email address.

BETA_CAPTURE_BOTH = True, will use a form and require the user enter their
first name, last name, and email address.

Installation
============

Add ``beta`` to your ``INSTALLED_APPS`` and run syncdb.

Add the following to your urls.py:

```python
    url(r'^beta/', include('beta.urls')),
```

Using the example templates provided in the code, create your customized beta signup templates.

Managers
--------

The ``BetaSignup`` model has the following manager method to help out:

```python
BetaSignup.objects.contacted()
BetaSignup.objects.not_contacted()
BetaSignup.objects.registered()
BetaSignup.objects.not_registered()
```

Side Effects
------------

``django-beta`` listens for a signal on User creation and marks the
corresponding BetaSignup entry as 'registered'.


TODO
----

* Admin views to show beta registrations over time
* Management commands to simplify emailing the interested users
