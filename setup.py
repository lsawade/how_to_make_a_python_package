""" :noindex:
Setup.py file that governs the installatino process of
`how_to_make_a_python_package` it is used by
`conda install -f environment.yml` which will install the package in an
environment specified in that file.

"""
import os
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as testcommand

# Utility function to read the README.md file.
# Used for the long_description.  It's nice, because now 1) we have a top levelx
# README.md file and 2) it's easier to type in the README.md file than to put a raw
# string in below ...


# Function to read and output README into long decription
def read(fname):
    """From Wenjie Lei 2019"""
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except Exception as e:
        return "Can't open %s" % fname


long_description = "%s" % read("README.md")


# This installs the pytest command. Meaning that you can simply type pytest
# anywhere and "pytest" will look for all available tests in the current
# directory and subdirectories recursively
class PyTest(testcommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        testcommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest
        import sys
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# Note that we are not specifying the requirements here because it is easier
# to specify them in the environment.yml
setup(
    name="how_to_make_a_python_package",
    description="A primer on how to set up your python code",
    long_description=long_description,
    version="0.0.1",
    author="Lucas Sawade",
    author_email="lsawade@princeton.edu",
    license='GNU Lesser General Public License, Version 3',
    keywords="Global CMT, Inversion, Moment Tensor",
    url='https://github.com/lsawade/how_to_make_a_python_package',
    packages=find_packages(),
    package_dir={"": "."},
    include_package_data=True,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    zip_safe=False,
    classifiers=[
        "Development Status :: Alpha",
        "Topic :: Utilities",
        "License :: GNU License",
    ]
)
