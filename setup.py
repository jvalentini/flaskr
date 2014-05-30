from setuptools import setup, find_packages

version = '0.0.1'

with open('requirements.txt') as f:
    requires = f.read().strip().splitlines()

if __name__ == '__main__':
    setup(
        name='flaskr',
        version=version,
        author='Justin Valentini',
        author_email='justin.valentini@gmail.com',
        packages=find_packages(),
        install_requires=requires
    )
