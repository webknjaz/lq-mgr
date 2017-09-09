#! /usr/bin/env python
"""Distribution setup module."""

__requires__ = ('setuptools >=36.3.0', )
"""The list of pre-requisite requirements, needed to run this module."""

from setuptools import setup

__name__ == '__main__' and setup(use_scm_version=True)
