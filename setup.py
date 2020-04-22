#!/usr/bin/env python

import os

import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name='megahal',
    author='Chris Jones, Robert Huselius',
    author_email='robert@huseli.us',
    url='https://github.com/Eboreg/megahal',
    description='Python implementation of megahal markov bot (fork)',
    license='BSD',
    version='0.3.2',
    py_modules=['megahal'],
    scripts=['scripts/megahal'],
    install_requires=["python-Levenshtein"],
    python_requires=">=3.6",
    packages=["megahal"],

    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules'])
