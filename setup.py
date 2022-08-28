#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

setup(
    name='hakxcore',
    version=__import__('hakxcore').__version__,
    description='Hakxcore personal Repo and python package',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Mukesh Kumar',
    author_email='mukeshkumarchark@gmail.com',
    license='MIT Licence',
    url='https://github.com/hakxcore/hakxcore',
    download_url='https://github.com/hakxcore/hakxcore/archive/refs/heads/main.zip',
    zip_safe=False,
    packages=find_packages(),
    install_requires=[
        'future',
        'terminaltables',
        'colorama'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'hakxcore = hakxcore.__main__'
        ]
    },
    keywords=['hakxcore', 'bug bounty', 'mukesh', 'pentesting', 'security', 'development', 'enterprenurship'],
)
