#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="wigle",
    version="0.0.3",
    author="Stanisław Pitucha",
    author_email="viraptor@gmail.com",
    description="Interface to wigle website",
    license="MIT",
    install_requires=["requests"],
    keywords="wigle wifi api search",
    url='https://github.com/viraptor/wigle',
    entry_points={'console_scripts': [
        'wigle_user_info=wigle.cmd:user_info',
        'wigle_search=wigle.cmd:search',
        ]},
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
        ]
    )
