import os
from setuptools import setup, find_packages

from beta import VERSION


f = open(os.path.join(os.path.dirname(__file__), 'README.txt'))
readme = f.read()
f.close()

setup(
    name='django-beta',
    version=".".join(map(str, VERSION)),
    description='django-beta is a reusable Django application for handling pre-beta signups.',
    long_description=readme,
    author='Frank Wiles',
    author_email='frank@revsys.com',
    url='http://github.com/revsys/django-beta/tree/master',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    test_suite='beta.tests.runtests.runtests'
)

