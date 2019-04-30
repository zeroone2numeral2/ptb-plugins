import os
from setuptools import setup


VERSION = '0.0.2'


def read_readme():
    with open("README.md", "r") as f:
        long_description = f.read()

    return long_description


setup(
    name='ptbplugins',
    version=VERSION,
    description='Simple util to import python-telegram-bot handlers using decorators',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/zeroone2numeral2/ptb-plugins',
    download_url='https://github.com/zeroone2numeral2/ptb-plugins/tarball/' + VERSION,
    author='zeroone2numeral2',
    author_email='numeralzeroone@gmail.com',
    license='MIT',
    packages=['ptbplugins'],
    install_requires=[
        'python-telegram-bot == 11.1.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
