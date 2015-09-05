# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements

version = '0.3.2'

requirements = parse_requirements('requirements.txt', session=False)

setup(
    name='potaje',
    version=version,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[str(r.req) for r in requirements],
    entry_points={
        'console_scripts': [
            'manage = potaje.manage:do_manage',
        ],
    },
)
