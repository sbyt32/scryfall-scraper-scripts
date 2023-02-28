from setuptools import setup, find_packages

setup(
    name='scryfallscraper',
    version='0.0.2',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
)