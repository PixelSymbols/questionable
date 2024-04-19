from setuptools import setup, find_packages
import os

current_path = os.path.abspath(os.path.dirname(__file__))

def read_file(*parts):
    with open(os.path.join(current_path, *parts), encoding='utf-8') as reader:
        return reader.read()

VERSION = '1.0.0'
DESCRIPTION = "A simple python package to pick non-empty value from 2 options."

# Setting up
setup(
    name="questionable",
    version=VERSION,
    url="https://github.com/PixelSymbols/questionable/",
    license="MIT",
    author="PixelSymbols",
    author_email="pixelsymbols@gmail.com",
    description=DESCRIPTION,
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'is empty', 'is value', 'option'],
    classifiers=[
        "Development Status :: 1 - Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)