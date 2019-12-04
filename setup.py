# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in Nthemes/__init__.py
from Nthemes import __version__ as version

setup(
	name='Nthemes',
	version=version,
	description='Material UI for ERPNext',
	author='Jawahar R Mallah',
	author_email='jawahar.mallah@netmanthan.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
