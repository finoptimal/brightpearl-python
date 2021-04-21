import os
from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = '0.11'

setup(
    name='brightpearl',
    version=VERSION,

    packages=find_packages(),

    # Forked from:
    #url='https://github.com/demystify-systems/brightpearl-python',
    url="https://github.com/finoptimal/brightpearl-python", 
    # Original:
    #author='Demystify Systems',
    #author_email='prod@dmstfy.com',
    author="FinOptimal",
    author_email="developer@finoptimal.com",
    description='Python client library for Brightpearl API : https://www.brightpearl.com',
    long_description=read('README.md'),
    license='MIT',

    keywords=['brightpearl', 'api', 'client'],
)
