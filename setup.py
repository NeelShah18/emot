#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
Setup script for emo
"""


from codecs import open
import os

from setuptools import setup


with open('README.rst', encoding='utf-8') as f:
    readme_content = f.read().strip()

setup(
    name='emo',
    author='Neel Shah',
    author_email='neelknightme@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT ',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description="Emoji and Emoticons detection package for Python",
    keywords=['emoji, emoticons'],
    extras_require={
        'dev': [
            'nose',
            'coverage',
            'coveralls'
        ]
    },
    include_package_data=True,
    license="New MIT",
    long_description=readme_content,
    packages=['emo'],
    url="",
    version="V1.0",
    zip_safe=True,
)
