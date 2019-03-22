from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA  python package',
    long_description=open('README.md').read(),
    url='https://github.com/Thamsanqa7/mypackage',
    author='Thamsanqa',
    author_email='thamsanqaqobisa@gmail.com'
)
