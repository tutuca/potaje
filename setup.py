# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = "0.5.2"


setup(
    name="potaje",
    url="https://github.com/tutuca/potaje",
    author="tutuca",
    author_email="maturburu@gmail.com",
    version=version,
    package_data={"static": ["*"], "templates": ["*.html"]},
    packages=find_packages(),
    install_requires=[
        "django-environ",
        "Django",
        "mistune",
        "Pillow",
        "requests",
        "restless",
    ],
    entry_points={"console_scripts": ["potaje = potaje.manage:do_manage"]},
)
