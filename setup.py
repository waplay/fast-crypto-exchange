import os
from setuptools import setup, find_packages
from src.version import __version__

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

ui = [os.path.join('src/ui', file) for file in os.listdir('src/ui')]

setup(
    license='Apache 2.0',
    name='fast-crypto-exchange',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    data_files=[('src/ui', ui)],
    entry_points={
        'gui_scripts': [
            'fast-crypto-exchange = src.main:main',
        ],
    },
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)