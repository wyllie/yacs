from setuptools import setup, find_packages

setup(
    name='Yacs',
    description='Yet Another CowSay',
    author='Andrew Wyllie',
    author_email='wyllie@dilex.net',
    version='1.0.1',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    license='MIT License',
    long_description=open('README.md').read()
)
