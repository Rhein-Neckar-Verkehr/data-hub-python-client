from setuptools import setup, find_packages

setup(
   name='data_hub_python_client',
   version='0.1',
   description='A simple client for the RNV data-hub API in python',
   author='Johannes Stegmüller',
   license='MIT',
   author_email='j.stegmueller@rnv-online.de',
   packages=find_packages(),
   requires=['setuptools'],
   install_requires=['setuptools', 'requests', 'dotenv'],
   python_requires='>=3.6'
)