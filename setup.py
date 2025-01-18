# setup.py
from setuptools import setup, find_packages

setup(
    name="graphUtilscd_harshita",
    version="1.0.0",
    description="A Python package for graph algorithms",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Harshita",
    author_email="harshita19062004@gmail.com",
    url="https://github.com/cdHarshita/graphUtilscd_harshita",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
