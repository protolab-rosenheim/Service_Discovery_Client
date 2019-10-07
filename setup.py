from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='SD_Client',
    version='1.0.0',
    description='Service Discovery Client, proto_lab',
    long_description=readme,
    author='proto_lab',
    author_email='kontakt@proto-lab.de',
    url='http://protolab-rosenheim.de/',
    license=license,
)

