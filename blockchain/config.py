"""
blockchain development configuration

Created by Shibo Chen, Data:1/26/2018
University of Michigan, class of 2019
email: chshibo@umich.edu
"""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\x88s\xbb lg\xf8\\\xfc\x0b5\xab\xa3\x06\x168\x96\x19\xfe\xa0S\xae\x0e\n'  # noqa: E501  pylint: disable=line-too-long
DIFFICULTY = 3

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'blockchain.sqlite3'
)
