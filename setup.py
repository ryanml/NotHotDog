from setuptools import setup

setup(
    name='nothotdog',
    version='0.0.1',
    packages=['nothotdog'],
    include_package_data=True,
    install_requires=[
        'boto3',
        'flask',
        'jsonify'
    ],
    maintainer='Ryan Lanese'
)