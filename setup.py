from setuptools import setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name='lisql',
    version='1.0.0',
    description='SQL companion library',
    py_modules=["lisql"],
    package_dir={'': 'src'}
)