# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.5'

dependencies = [
    'Django',
    'restless',
    'requests'
]

setup(
    name='potaje',
    version=version,
    include_package_data=True,
    packages=find_packages(),
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'manage = potaje.manage:do_manage',
        ],
    },
)
