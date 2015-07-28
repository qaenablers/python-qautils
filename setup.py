# -*- coding: utf-8 -*-

"""
    setup.py script install QA-Utils
"""

__author__ = "@jframos"
__project__ = "python-qautils [https://github.com/qaenablers/python-qautils]"
__copyright__ = "Copyright 2015"
__license__ = " Apache License, Version 2.0"
__version__ = "1.1.0"

from setuptools import setup
from setuptools import find_packages
from pip.req import parse_requirements

REQUIREMENTS_FILE = "requirements.txt"


# Get requirements list from requirements.txt file
# > parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(REQUIREMENTS_FILE, session=False)
# > requirements_list is a list of requirement; e.g. ['requests==2.6.0', 'Fabric==1.8.3']
requirements_list = [str(ir.req) for ir in install_reqs]

setup(name='python-qautils',
      version='1.1.0',
      description='QAUtils. Utilities for Software Quality Assurance - Python',
      author='@jframos',
      license='Apache 2.0',
      url='https://github.com/qaenablers/python-qautils',
      keywords=['qa', 'qautils', 'utils', 'quality'],
      packages=find_packages(),
      install_requires=requirements_list)
