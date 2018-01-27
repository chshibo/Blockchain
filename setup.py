"""
BlockChain API Configuration

Created by Shibo Chen, Data:1/26/2018
University of Michigan, class of 2019
email: chshibo@umich.edu
"""
from setuptools import setup

setup(
    name='blockchain',
    version='0.1.0',
    packages=['blockchain'],
    include_package_data=True,
    install_requires=[
        'Flask==0.12.2',
        'sh==1.12.14'
    ],
)
