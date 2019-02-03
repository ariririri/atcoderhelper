#!/usr/bin/env python
from setuptools import setup, find_packages


requirements = {
    'install': [
        'setuptools',
        'beautifulsoup4',
        'certifi',
        'urllib3',
        'typing',
        'typing_extensions',
        'filelock',
    ],
    'stylecheck': [
        'autopep8>=1.4.1,<1.5',
        'flake8>=3.6,<3.7',
        'pbr==4.0.4',
        'pycodestyle>=2.4,<2.5',
    ],
    'test': [
        'pytest==4.1.1',  
        'mock',
    ]
}


extras_require = {k: v for k, v in requirements.items() if k != 'install'}
setup_requires = []
install_requires = requirements['install']
tests_require = requirements['test']



setup(
    name='atcoderhelper',
    version='0.0.1',
    description='Sample package for Python-Guide.org',
    license="mit",
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=install_requires
)
