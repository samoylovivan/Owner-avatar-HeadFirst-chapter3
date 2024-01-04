# Windows: C:\mymodules> py -3 setup.py sdist
# UNIX: mymodules$ python3 setup.py sdist

from setuptools import setup

setup (
    name='vsearch',
    version='1.0',
    description='The Head First Python Search Tools',
    author='HF Python 2e',
    author_email='hppy2e@gmail.com',
    url='headfirstlabs.com',
    py_modules=['vsearch'],
    )
