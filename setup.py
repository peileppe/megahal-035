#!/usr/bin/env python

"""Setup script for py-megahal"""


def main():
    from distutils.core import setup

    setup(
        name='megahal',
        author='Chris Jones, Robert Huselius',
        author_email='robert@huseli.us',
        url='http://gruntle.org/projects/python/megahal/',
        description='Python implementation of megahal markov bot (fork)',
        license='BSD',
        version='0.3',
        py_modules=['megahal'],
        scripts=['scripts/megahal'],
        install_requires=["python-Levenshtein", "emoji"],
        python_requires=">=3.6",

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

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
