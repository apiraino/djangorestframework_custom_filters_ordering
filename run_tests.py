# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys
from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            },
        },
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'djangorestframework_custom_filters_ordering',
            'tests',
        ),
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ),
        ROOT_URLCONF='tests.urls',
        USE_TZ=True,
        SECRET_KEY='foobar',
        REST_FRAMEWORK={
            'DEFAULT_FILTER_BACKENDS': [
                'djangorestframework_custom_filters_ordering.filters.RelatedOrderingFilter',
            ],
        }
    )


def runtests():
    argv = sys.argv[:1] + ['test'] + sys.argv[1:]
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
