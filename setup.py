from setuptools import setup, find_packages
import os

setup(
    # Application name:
    name="runeatest",

    # Version number:
    version="0.0.1",

    # Application author details:
    author="Sabin IO",
    author_email="hello@sabin.io",

    # Packages
    packages=find_packages(),

    # Data files
    include_package_data=True,
    zip_safe=False,

    # Details
    url="https://github.com/RichieBzzzt/runeatest",

    description="nunit test report generator to run in DataBricks",
    with open("README.md", "r") as fh:
    long_description = fh.read()
    keywords='azure, databricks, nunit',

     classifiers=[
    'Development Status :: 1 - Planning',      
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
