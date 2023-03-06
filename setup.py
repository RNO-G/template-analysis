#!/usr/bin/env python

from setuptools import setup

setup(name='template_analysis', # rename to the name of your analysis
      version='0.1', # increase as needed while developing your code
      description='RNO-G template analysis repository', # replace by useful description of the project
      url='http://github.com/RNO-G/template-analysis',
      author='The RNO-G Collaboration, Steffen Hallmann', # put your name
      author_email='steffen.hallmann@desy.de', # put your email adress
      license='MIT',
      packages=['template_analysis'], # put the sub directory where your analysis sits
      entry_points = {'console_scripts': ["run-template-analysis=template_analysis.run:main"]}, #edit and add more commands to the list if need be
      zip_safe=False)
