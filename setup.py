#!/usr/bin/env python
# -*- Coding: utf-8 -*-
"""
Setup file...

Python requires >= 3.9

Author: Dario sotelo
Date: 15/12/2021
"""
from distutils.core import setup


setup(
      name='api_bot',
      version='1.0',
      description='Package bot for testing',
      author='Dario Sotelo',
      author_email='dariosotelo3@gmail.com',
      package_dir={
            '': 'bot',
      },
      classifiers=[
            'Programming Language :: Python :: >= 3.9'
      ]
)
