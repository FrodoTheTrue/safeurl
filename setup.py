from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='SafeUrl',
    version='0.0.3',
    packages=find_packages(),
    # long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'requests==2.7.0'
    ],
    test_suite='tests',
)