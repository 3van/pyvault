#!/usr/bin/env python
import os
import sys
from setuptools import setup

requirements = [
	'requests',
]

exec(open('pyvault/version.py').read())

setup(
	name="pyvault",
	version=version,
	description="Python client for HashiCorp's Vault",
	url='https://github.com/3van/pyvault',
	packages=[
		'pyvault'
	],
	install_requires=requirements,
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Other Environment',
		'Intended Audience :: Developers',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Topic :: Security',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: System :: Systems Administration',
		'Topic :: Utilities'
	],
)