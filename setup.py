from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bitalg',
    description='Laboratory classes in the Geometric Algorithms course for Computer Science students at the AGH University.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='AGH BIT Student Scientific Group',
    packages=['bitalg'],
    python_requires='>=3.11'
)