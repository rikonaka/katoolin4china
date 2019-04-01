#!/usr/bin/env python3

import setuptools


setuptools.setup(

    name="k4c",

    version="1.61",

    license="GPL-2.0",

    author="rikonaka",
    author_email="xxy1836@gmail.com",

    install_requires=[
    ],

    packages=[
        "k4c",
    ],

    entry_points={
        "console_scripts": [
            "k4c = k4c.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)
