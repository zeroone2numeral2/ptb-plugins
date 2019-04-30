import os
from setuptools import setup


def read_readme():
    with open("README.md", "r") as f:
        long_description = f.read()

    return long_description


setup(
    name='ptbplugins',
    version='0.0.1',
    description='Simple util to import python-telegram-bot handlers using decorators',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/zeroone2numeral2/ptb-plugins',
    author='zeroone2numeral2',
    license='MIT',
    packages=['ptbplugins'],
    install_requires=[
        'python-telegram-bot == 11.1.0',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe=False
)
