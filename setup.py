# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def readme():
    with open("README.txt") as f:
        return f.read()


version = "0.5.0"


setup(
    name="django-recaptcha3",
    packages=find_packages(exclude=["samples"]),
    include_package_data=True,
    version=version,
    install_requires=["requests"],
    tests_require=(["django-setuptest"],),
    test_suite="setuptest.setuptest.SetupTestSuite",
    description="Django reCaptcha v3 field/widget",
    long_description=readme(),
    author="Andrea Briganti",
    author_email="kbytesys@gmail.com",
    url="https://github.com/nextsux/django-recaptcha3",
    download_url="https://github.com/nextsux/django-recaptcha3/tarball/v%s" % version,
    keywords=["django", "recaptcha", "recaptcha3"],
    license="GNU LGPL v2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
