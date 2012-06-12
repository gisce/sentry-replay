#!/usr/bin/env python
"""
sentry-irc
==============

An extension for Sentry which integrates with sends events to another Sentry
instance.

:copyright: (c) 2012 by Eduard Carreras, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=4.6.0',
]

setup(
    name='sentry-replay',
    version='0.1.0',
    author='Eduard Carreras',
    author_email='ecarreras@gisce.net',
    url='http://code.gisce.net/sentry-replay',
    description='A Sentry extension which replay events to other Sentry',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
       'sentry.plugins': [
            'replay = sentry_replay.plugin:Replay'
        ],
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
