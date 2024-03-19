from setuptools import setup

setup(
   name='data-hub-python-client',
   version='0.1',
   description='A simple client for the RNV data-hub API in python',
   author='Johannes Stegmüller',
   license='MIT',
   author_email='j.stegmueller@rnv-online.de',
   packages=['data-hub-python-client'],
   install_requires=['requests'],
)