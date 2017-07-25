# Nested related entities filter for DRF OrderingFilter

A custom DRF OrderingFilter with support to nested related fields.

Still work in progress (a.k.a. "works for me")

## Build

`python setup.py bdist_wheel`

## Requirements

At the moment Django >= 1.10, DRF probably >= 3.x. Python 2.7 and 3.x (not tested yet).

## Installation

`pip install dist/djangorestframework_custom_filters_ordering-X.Y.Z-py2.py3-none-any.whl`

## Usage

See `example_app/views.py`

## Run tests

`cd example_app`

`python manage test example_app`

## Reference

[DRF issue on Github](https://github.com/encode/django-rest-framework/issues/1005)

Kudos to [rhunwicks](https://github.com/rhunwicks) for the initial patch.

--> **PR and suggestions welcome!**
