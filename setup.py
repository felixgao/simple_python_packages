from setuptools import setup, find_packages
import os

version = "0.0.1" #overwrite this
package_name = "name.somepackage" #overwrite this
author = "yourname" #overwrite this
email = "yourname@yourorg.com" #overwrite this
keywords = "" # this is a list of keywords that can be used to search for in pypi

setup(name=package_name,
    version=version,
    description="A package description",
    long_description="""The package's long description""",
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords=keywords,
    author=author,
    author_email=email,
    url='http://www.yourwebsite.com/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=[package_name.split(".")[0]], # see http://pythonhosted.org/distribute/setuptools.html#namespace-packages
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
      # -*- Extra requirements: -*-
      ],
    entry_points="""
      # -*- Entry points: -*-
      """,
    )
