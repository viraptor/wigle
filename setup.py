#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="wigle",
    version="0.0.1",
    author="Stanisław Pitucha",
    author_email="viraptor@gmail.com",
    description="Interface to wigle website",
    license="MIT",
    install_requires=["requests"],
    keywords="wigle wifi api search",
    entry_points={'console_scripts': [
        'wigle_user_info=wigle.cmd:user_info',
        'wigle_search=wigle.cmd:search',
        ]},
    packages=find_packages(),
    )
