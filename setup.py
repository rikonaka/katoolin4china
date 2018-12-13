#!/usr/bin/env python3

import setuptools


setuptools.setup(

    name="k4c",

    version="1.6",

    license="GPL-2.0",

    author="isinstance",
    author_email="xxy1836@gmail.com",

    install_requires=[
    ],

    packages=[
        "k4c",
    ],

    entry_points={
        "console_scripts": [
            "k4c = katoolin4china.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)
