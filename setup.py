# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements

version = '0.5.2'

requirements = parse_requirements('requirements.txt', session=False)

setup(
    name='potaje',
    url='https://github.com/tutuca/potaje',
    author='tutuca',
    author_email='maturburu@gmail.com',
    version=version,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[str(r.req) for r in requirements],
    entry_points={
        'console_scripts': [
            'potaje = potaje.manage:do_manage',
        ],
    },
)
