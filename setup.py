# -*- coding: utf-8 -*-

from setuptools import setup

version = '0.1'


setup(version=version,
    name='Gematria-API',
    description="Gematria and Isopsephy calculator",
    author='Raphael Enochian',
    author_email="raphael.enochian@scryptmail.com",
    packages=[
        "gematria_api",
        "gematria_api.tests",
        # "gematria_api.utils",
    ],
    scripts=[
        "bin/manage.py",
    ],
    long_description="""""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',

    install_requires=[
        "Flask==0.10.1",
        "Flask-Script==2.0.5",
        # "Flask-Admin==1.3.0",
        # "Flask-Security==1.7.4",
        "Flask-RESTful==0.3.4",
        "Flask-Testing==0.4.2",
        "marshmallow==2.2.0",

        # Dev tools
        "nose",
        "ipython",
        "ipdb",
        # "pysqlite==2.6.3"
        # "marshmallow==1.2.6",
    ],
    zip_safe=False,
)
