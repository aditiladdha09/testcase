from setuptools import setup, find_packages

setup(
    name="api-automation-karate",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'karate',
        'pyyaml',
        'jsonschema',
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
        ],
    },
    entry_points={
        'console_scripts': [
            'generate_tests=scripts.generate_tests:main',
        ],
    },
)
