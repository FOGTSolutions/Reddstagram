from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Automated Reddit to Instagram'
LONG_DESCRIPTION = 'A package for automated Reddit subforum scraping and uploading to Instagram.'

# Setting up
setup(
    name="reddstagram",
    version=VERSION,
    author="FOGT Solutions",
    author_email="<contact@fogt-solutions.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'instagram', 'reddit', 'reddstagram'],
)