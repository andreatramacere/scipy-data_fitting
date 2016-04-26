from setuptools import find_packages, setup

from scipy_data_fitting import __version__

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='scipy-data_fitting',
    version=__version__,
    author='Evan Sosenko',
    author_email='razorx@evansosenko.com',
    packages=find_packages(exclude=['docs']),
    url='https://github.com/razor-x/scipy-data_fitting',
    license='MIT',
    description='Complete pipeline for easy data fitting with Python.',
    long_description=long_description,
    test_suite='nose2.collector.collector',
    install_requires=[
    ]
)
