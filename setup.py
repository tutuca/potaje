# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.5.2'


setup(
    name='potaje',
    url='https://github.com/tutuca/potaje',
    author='tutuca',
    author_email='maturburu@gmail.com',
    version=version,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'Django',
        'Pillow',
        'requests',
        'restless',
        'django-environ',
        'mistune'
    ],
    entry_points={
        'console_scripts': [
            'potaje = potaje.manage:do_manage',
        ],
    },
)
