#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(name='template_analysis', # rename to the name of your analysis
      version='0.1', # increase as needed while developing your code
      description='RNO-G template analysis repository', # replace by useful description of the project
      url='http://github.com/RNO-G/template-analysis',
      author='The RNO-G Collaboration, Steffen Hallmann', # put your name
      author_email='steffen.hallmann@desy.de', # put your email adress
      license='MIT',
      packages=find_packages(), # alternatively, put the list of sub directories where your analyses sit
      #entry_points = {'console_scripts': ["run-template-analysis=template_analysis.run:main"]}, #uncomment and add more commands to the list if need be
      zip_safe=False)
