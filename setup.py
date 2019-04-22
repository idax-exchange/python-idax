#!/usr/bin/env python
# encoding: utf-8
"""
@author: jension
@license: Node Supply Chain Manager Corporation Limited.
@contact: 1490290160@qq.com
@software: garner
@file: setup.py
@time: 2019/3/27 15:09
@desc:
"""
from setuptools import setup

setup(
    name='python-idax',
    version='0.0.1',
    packages=['idax'],
    description='IDAX REST API python implementation',
    url='',
    author='jension',
    license='MIT',
    author_email='',
    install_requires=['requests', 'websocket-client',"pytest"],
    keywords='IDAX exchange rest api bitcoin ethereum btc eth neo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
