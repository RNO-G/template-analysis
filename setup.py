from setuptools import setup

setup(name='template_analysis',
      version='0.1',
      description='RNO-G template repository',
      url='http://github.com/RNO-G/template-analysis',
      author='The RNO-G Collaboration, Steffen Hallmann',
      author_email='steffen.hallmann@desy.de',
      license='MIT',
      packages=['template_analysis'],
      entry_points = {'console_scripts': ["run-template-analysis=template_analysis.run:main"]}, #add more to the list if need be
      zip_safe=False)
