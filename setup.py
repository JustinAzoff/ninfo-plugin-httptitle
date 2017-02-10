from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ninfo-plugin-httptitle',
    version=version,
    description="Fetch HTTP Titles",
    keywords='ninfo plugin http title',
    author='Justin Azoff',
    author_email='jazoff@illinois.edu',
    url='',
    license='',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo",
    ],
    entry_points = {
        'ninfo.plugin': [
            'httptitle    =   ninfo_plugin_httptitle'
        ]
    }
) 
