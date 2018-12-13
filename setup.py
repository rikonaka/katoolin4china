#!/usr/bin/env python3

import setuptools


setuptools.setup(

    name="katoolin4china",

    version="1.6",

    license="GPL-2.0",

    author="isinstance",
    author_email="xxy1836@gmail.com",

    install_requires=[
    ],

    packages=[
        "katoolin4china",
    ],

    entry_points={
        "console_scripts": [
            "k4c = katoolin.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)
